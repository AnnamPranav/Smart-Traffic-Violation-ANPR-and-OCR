import base64
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import cv2
import numpy as np

from backend.config import EVIDENCE_DIR
from backend.services.pipeline import TrafficPipeline
from backend.services.storage import recent_records

app=Flask(__name__)
CORS(app, resources={r"/api/*":{"origins":"*"}})
_pipeline=None

def get_pipeline():
    global _pipeline
    if _pipeline is None:
        _pipeline=TrafficPipeline()
    return _pipeline

@app.get("/api/health")
def health():
    return jsonify({"status":"ok","service":"Smart Traffic Violation + ANPR"})

@app.get("/api/history")
def history():
    return jsonify({"items":recent_records()})

@app.post("/api/detect")
def detect():
    if "image" not in request.files:
        return jsonify({"status":"error","message":"Please upload an image."}),400

    raw=request.files["image"].read()
    img=cv2.imdecode(np.frombuffer(raw,np.uint8),cv2.IMREAD_COLOR)
    if img is None:
        return jsonify({"status":"error","message":"Invalid image."}),400

    signal=request.form.get("signal","RED").upper()
    try:
        record, annotated=get_pipeline().process(img,signal)
        ok,buf=cv2.imencode(".jpg",annotated)
        encoded=base64.b64encode(buf.tobytes()).decode() if ok else None
        record["image_base64"]=encoded
        record["status"]="success"
        return jsonify(record)
    except Exception as exc:
        app.logger.exception("Detection failed")
        return jsonify({"status":"error","message":str(exc)}),500

@app.get("/evidence/<path:filename>")
def evidence(filename):
    return send_from_directory(EVIDENCE_DIR,filename)

@app.get("/")
def frontend():
    return send_from_directory("../frontend","index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(__import__("os").getenv("PORT","5000")),debug=True)
