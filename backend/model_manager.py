import urllib.request
from pathlib import Path
from backend.config import VEHICLE_MODEL, PLATE_MODEL, PLATE_MODEL_URL

def _download(url: str, target: Path):
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".part")
    urllib.request.urlretrieve(url, tmp)
    tmp.replace(target)

def ensure_models():
    if not VEHICLE_MODEL.exists():
        # Ultralytics can download yolov8n automatically when YOLO("yolov8n.pt") is called.
        pass
    if not PLATE_MODEL.exists() or PLATE_MODEL.stat().st_size < 1_000_000:
        _download(PLATE_MODEL_URL, PLATE_MODEL)
    return str(VEHICLE_MODEL), str(PLATE_MODEL)
