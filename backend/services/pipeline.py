import uuid
from datetime import datetime, timezone
import cv2
import numpy as np

from backend.services.detector import TrafficDetector
from backend.services.ocr import PlateOCR
from backend.services.violation import evaluate
from backend.services.storage import save_evidence, save_record

class TrafficPipeline:
    def __init__(self):
        self.detector=TrafficDetector()
        self.ocr=PlateOCR()

    def process(self, image, signal="RED"):
        vehicles=self.detector.detect_vehicles(image)
        plates=self.detector.detect_plates(image)

        ocr_results=[]
        for plate in plates:
            x1,y1,x2,y2=plate["bbox"]
            crop=image[max(0,y1):max(0,y2),max(0,x1):max(0,x2)]
            text,conf=self.ocr.read(crop)

            matched_vehicle=None
            for v in vehicles:
                if self.detector.inside(plate,v):
                    matched_vehicle=v
                    break

            ocr_results.append({
                "plate":text,
                "ocr_confidence":round(conf,4),
                "plate_confidence":plate["confidence"],
                "plate_bbox":plate["bbox"],
                "vehicle":matched_vehicle
            })

        violations=evaluate(vehicles,signal)
        annotated=self.detector.annotate(image,vehicles,plates,ocr_results,violations)

        primary_plate=None
        if ocr_results:
            best=max(ocr_results,key=lambda x:x["ocr_confidence"])
            primary_plate=best["plate"]

        record_id=uuid.uuid4().hex[:12]
        ts=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        safe_plate=(primary_plate or "UNREADABLE").replace("/","_")
        evidence=f"{safe_plate}_{ts}_{record_id}.jpg"
        evidence_name=save_evidence(annotated,evidence)

        record={
            "id":record_id,
            "plate":primary_plate,
            "plate_confidence":max([r["ocr_confidence"] for r in ocr_results],default=0),
            "vehicles":vehicles,
            "plates":ocr_results,
            "violations":violations,
            "signal":signal.upper(),
            "evidence_image":evidence_name,
            "timestamp":datetime.now(timezone.utc).isoformat()
        }
        save_record(record)
        return record, annotated
