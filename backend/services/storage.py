import json
from datetime import datetime, timezone
from pathlib import Path
from backend.config import LOG_FILE, EVIDENCE_DIR

def save_evidence(image, filename):
    path=EVIDENCE_DIR/filename
    import cv2
    cv2.imwrite(str(path), image)
    return path.name

def save_record(record):
    try:
        existing=json.loads(LOG_FILE.read_text())
        if not isinstance(existing,list): existing=[]
    except Exception:
        existing=[]
    record=dict(record)
    record["created_at"]=datetime.now(timezone.utc).isoformat()
    existing.append(record)
    LOG_FILE.write_text(json.dumps(existing,indent=2))
    return record

def recent_records(limit=25):
    try:
        data=json.loads(LOG_FILE.read_text())
        return data[-limit:][::-1]
    except Exception:
        return []
