import urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
models=ROOT/"backend"/"models"
models.mkdir(parents=True,exist_ok=True)
url="https://github.com/Muhammad-Zeerak-Khan/Automatic-License-Plate-Recognition-using-YOLOv8/raw/main/license_plate_detector.pt"
target=models/"license_plate_detector.pt"
if not target.exists():
    print("Downloading dedicated license-plate YOLO model...")
    urllib.request.urlretrieve(url,target)
    print("Saved",target)
else:
    print("Plate model already exists.")
