import re
import cv2
import numpy as np
import easyocr

class PlateOCR:
    def __init__(self):
        self.reader = easyocr.Reader(["en"], gpu=False, verbose=False)

    @staticmethod
    def normalize(text):
        return re.sub(r"[^A-Z0-9]", "", text.upper())

    @staticmethod
    def valid_indian_plate(text):
        # General private/commercial Indian registration shape.
        return bool(re.match(r"^[A-Z]{2}\d{1,2}[A-Z]{1,3}\d{3,4}$", text))

    def read(self, crop):
        if crop is None or crop.size == 0:
            return None, 0.0

        h,w=crop.shape[:2]
        if h < 5 or w < 10:
            return None, 0.0

        scale=max(2.0, 100.0/h)
        resized=cv2.resize(crop,None,fx=scale,fy=scale,interpolation=cv2.INTER_CUBIC)
        gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
        gray=cv2.bilateralFilter(gray,7,50,50)
        variants=[
            resized,
            gray,
            cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        ]

        candidates=[]
        for variant in variants:
            results=self.reader.readtext(
                variant,
                allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                detail=1,
                paragraph=False
            )
            for _,text,conf in results:
                cleaned=self.normalize(text)
                if len(cleaned)>=5 and conf>=0.20:
                    score=float(conf)+(0.25 if self.valid_indian_plate(cleaned) else 0)
                    candidates.append((score,cleaned,float(conf)))

        if not candidates:
            return None,0.0
        _,text,conf=max(candidates,key=lambda x:x[0])
        return text,conf
