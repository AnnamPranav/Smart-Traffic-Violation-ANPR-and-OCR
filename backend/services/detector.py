from pathlib import Path
import cv2
from ultralytics import YOLO

from backend.model_manager import ensure_models

VEHICLE_CLASSES = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}

class TrafficDetector:
    def __init__(self):
        vehicle_path, plate_path = ensure_models()
        self.vehicle_model = YOLO(vehicle_path)
        self.plate_model = YOLO(plate_path)

    def detect_vehicles(self, image, conf=0.35):
        result = self.vehicle_model(
            image,
            verbose=False,
            classes=list(VEHICLE_CLASSES.keys()),
            conf=conf
        )[0]
        items=[]
        for box in result.boxes:
            x1,y1,x2,y2=map(int, box.xyxy[0])
            cls=int(box.cls[0])
            score=float(box.conf[0])
            items.append({
                "bbox":[x1,y1,x2,y2],
                "class_id":cls,
                "class_name":VEHICLE_CLASSES.get(cls,"vehicle"),
                "confidence":round(score,4)
            })
        return items

    def detect_plates(self, image, conf=0.25):
        result=self.plate_model(image, verbose=False, conf=conf)[0]
        items=[]
        for box in result.boxes:
            x1,y1,x2,y2=map(int, box.xyxy[0])
            score=float(box.conf[0])
            items.append({
                "bbox":[x1,y1,x2,y2],
                "confidence":round(score,4)
            })
        return items

    @staticmethod
    def inside(plate, vehicle):
        px1,py1,px2,py2=plate["bbox"]
        vx1,vy1,vx2,vy2=vehicle["bbox"]
        cx=(px1+px2)/2
        cy=(py1+py2)/2
        return vx1<=cx<=vx2 and vy1<=cy<=vy2

    def annotate(self, image, vehicles, plates, ocr_results, violations):
        out=image.copy()
        for v in vehicles:
            x1,y1,x2,y2=v["bbox"]
            cv2.rectangle(out,(x1,y1),(x2,y2),(0,255,0),2)
            label=f'{v["class_name"]} {v["confidence"]:.0%}'
            cv2.putText(out,label,(x1,max(20,y1-8)),
                        cv2.FONT_HERSHEY_SIMPLEX,0.55,(0,255,0),2)

        for p in plates:
            x1,y1,x2,y2=p["bbox"]
            cv2.rectangle(out,(x1,y1),(x2,y2),(0,220,255),2)

        for r in ocr_results:
            p=r["plate_bbox"]
            x1,y1,x2,y2=p
            text=f'{r["plate"] or "UNREADABLE"} {r["ocr_confidence"]:.0%}'
            cv2.rectangle(out,(x1,y1),(x2,y2),(255,0,255),2)
            cv2.putText(out,text,(x1,max(20,y1-8)),
                        cv2.FONT_HERSHEY_SIMPLEX,0.65,(255,0,255),2)

        banner=" | ".join(violations)
        cv2.rectangle(out,(0,0),(out.shape[1],42),(15,18,28),-1)
        cv2.putText(out,banner,(12,28),cv2.FONT_HERSHEY_SIMPLEX,0.65,
                    (0,220,255) if violations==["No Violation"] else (0,0,255),2)
        return out
