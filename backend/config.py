import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "backend" / "models"
EVIDENCE_DIR = Path(os.getenv("EVIDENCE_DIR", str(ROOT / "data" / "evidence")))
LOG_FILE = Path(os.getenv("LOG_FILE", str(ROOT / "data" / "violations.json")))

VEHICLE_MODEL = MODEL_DIR / "yolov8n.pt"
PLATE_MODEL = MODEL_DIR / "license_plate_detector.pt"

PLATE_MODEL_URL = os.getenv(
    "PLATE_MODEL_URL",
    "https://github.com/Muhammad-Zeerak-Khan/"
    "Automatic-License-Plate-Recognition-using-YOLOv8/raw/main/"
    "license_plate_detector.pt"
)

EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
