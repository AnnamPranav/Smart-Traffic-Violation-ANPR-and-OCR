# 🚦 Smart Traffic Violation — ANPR & OCR

An AI-powered traffic monitoring system that combines **YOLO-based vehicle detection**, **dedicated license-plate detection**, **EasyOCR**, and traffic-rule analysis to identify and record potential traffic violations from images.

The project includes a browser-based frontend and a Python Flask backend.

---

## ✨ Features

- 🚗 Vehicle detection using YOLO
- 🔎 Dedicated license-plate detection using YOLO
- 🔤 Real license-plate OCR using EasyOCR
- 🇮🇳 Indian vehicle registration format validation
- 🆔 Vehicle/plate association
- 🚦 Traffic-signal violation analysis
- 🪖 Possible no-helmet detection heuristic
- 📸 Evidence image generation
- 📋 Violation logging
- 📊 OCR confidence reporting
- 🌐 Browser-based dashboard
- 🔌 REST API
- 💻 Local development support
- ☁️ Deployment-ready architecture

> **Important:** The current helmet feature is a heuristic and should not be represented as a production-grade helmet detector without a dedicated helmet-detection model.

---

# 🧠 System Architecture

```text
                    Traffic Image
                         │
                         ▼
              ┌─────────────────────┐
              │ YOLO Vehicle        │
              │ Detection           │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ License Plate YOLO  │
              │ Detection           │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Plate Preprocessing │
              │ + Image Enhancement │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ EasyOCR             │
              │ Text Recognition    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Plate Validation    │
              │ + Confidence        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Traffic Violation   │
              │ Analysis            │
              └──────────┬──────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Evidence Image          Violation Log
              │                     │
              └──────────┬──────────┘
                         ▼
                  Frontend Result
```

---

# 🛠️ Technology Stack

## AI / Computer Vision

- Python
- YOLO
- Ultralytics
- OpenCV
- EasyOCR
- NumPy
- PyTorch

## Backend

- Flask
- REST API
- Python

## Frontend

- HTML
- CSS
- JavaScript
- Responsive browser interface

## Deployment

- GitHub
- Vercel — frontend
- Render / similar Python hosting — AI backend

---

# 📁 Project Structure

```text
Smart-Traffic-Violation-ANPR/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── detection.py
│   ├── number_plate.py
│   ├── violation.py
│   ├── models/
│   │   └── license_plate_detector.pt
│   └── ...
│
├── frontend/
│   └── ...
│
├── public/
│   └── ...
│
├── scripts/
│   └── download_models.py
│
├── data/
│   ├── evidence/
│   └── ...
│
├── requirements.txt
├── vercel.json
├── README.md
└── .gitignore
```

---

# 🚀 Run Locally

## 1. Clone the repository

```bash
git clone https://github.com/AnnamPranav/Smart-Traffic-Violation-ANPR-and-OCR.git
cd Smart-Traffic-Violation-ANPR-and-OCR
```

---

## 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Download the license-plate model

```bash
python scripts/download_models.py
```

The model will be saved under:

```text
backend/models/license_plate_detector.pt
```

---

## 5. Start the application

On macOS, port `5000` may be occupied by Control Center/AirPlay Receiver.

Use port `5001`:

```bash
python -c "from backend.app import app; app.run(host='0.0.0.0', port=5001, debug=True)"
```

Open:

```text
http://localhost:5001
```

---

# 🔍 How Detection Works

## Step 1 — Vehicle Detection

YOLO identifies vehicles in the input image.

Example:

```text
Car
Motorcycle
Truck
Bus
```

Each detection contains:

- Bounding box
- Class
- Confidence

---

## Step 2 — License Plate Detection

A dedicated YOLO license-plate model identifies the plate region instead of relying on random text generation or simple full-image OCR.

```text
Vehicle
   ↓
Plate Region
   ↓
OCR
```

This improves OCR accuracy because EasyOCR receives a focused plate image.

---

## Step 3 — OCR

EasyOCR extracts text from the detected plate.

Example:

```text
TS09AB1234
```

The system also records OCR confidence.

Example:

```text
Plate: TS09AB1234
OCR Confidence: 91.1%
```

---

## Step 4 — Plate Validation

The OCR result is normalized and checked against common Indian registration-number patterns.

This helps reduce obviously invalid OCR results.

---

# 🚦 Traffic Violation Detection

The system can evaluate traffic conditions such as:

### Red-light related violation

```text
Signal = RED
        +
Vehicle detected crossing/violating rule
        ↓
Potential violation
```

### Helmet

The current implementation can report:

```text
Possible No Helmet
```

This is a heuristic.

For production deployment, a dedicated helmet-detection YOLO model should be added.

---

# 📸 Evidence

When an event is detected, the system can generate an evidence image containing the relevant detection annotations.

The record can contain:

```json
{
  "plate": "TS09AB1234",
  "plate_confidence": 0.91,
  "violations": [
    "Red Light Violation"
  ],
  "timestamp": "2026-10-08_18-30-20"
}
```

---

# 🔌 API

## Health Check

```http
GET /health
```

or:

```http
GET /api/health
```

Example response:

```json
{
  "status": "running",
  "service": "Smart Traffic AI Backend",
  "ocr": "EasyOCR"
}
```

---

## Detect Traffic Violation

```http
POST /detect
```

or:

```http
POST /api/detect
```

Multipart form:

```text
image = traffic_image.jpg
signal = RED
```

Example response:

```json
{
  "status": "success",
  "plate": "TS09AB1234",
  "plate_confidence": 0.91,
  "plate_detected": true,
  "violations": [
    "Red Light Violation"
  ],
  "signal": "RED",
  "timestamp": "2026-10-08_18-30-20"
}
```

---

# 🖥️ Frontend

The frontend allows users to:

1. Upload a traffic image
2. Select the traffic signal state
3. Start analysis
4. View detected vehicles
5. View the recognized plate
6. View OCR confidence
7. View violations
8. View the annotated evidence image

Example:

```text
┌──────────────────────────────────────────┐
│         SMART TRAFFIC AI                 │
│                                          │
│ Traffic Signal: [ RED ▼ ]               │
│                                          │
│ [ Choose Traffic Image ]                 │
│                                          │
│        [ Analyze Image ]                │
│                                          │
│ Plate: TS09AB1234                        │
│ OCR Confidence: 91.1%                    │
│ Vehicles: 6                              │
│ Violation: Red Light Violation           │
│                                          │
│        [ Evidence Image ]                │
└──────────────────────────────────────────┘
```

---

# ☁️ Deployment Architecture

The AI backend uses heavy Python/ML dependencies such as:

- PyTorch
- YOLO
- EasyOCR
- OpenCV

Therefore the recommended production architecture is:

```text
                    GitHub
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
          Vercel               Render
        Frontend               Backend
             │                   │
             │    REST API       │
             └────────►──────────┘
                                 │
                    ┌────────────┴────────────┐
                    ▼                         ▼
                  YOLO                     EasyOCR
                    │                         │
                    └────────────┬────────────┘
                                 ▼
                        ANPR + Violation
```

## Frontend

Deploy the frontend on:

```text
Vercel
```

## Backend

Deploy the Flask/AI backend on:

```text
Render
```

or another persistent Python hosting service.

---

# 🌐 Render Backend

Recommended build command:

```bash
pip install -r requirements.txt
```

Recommended start command:

```bash
gunicorn -w 1 -b 0.0.0.0:$PORT backend.app:app
```

Make sure `gunicorn` is included in `requirements.txt`.

---

# 🔐 Environment Variables

Do not commit secrets.

Use:

```text
.env
```

for local development and configure production variables through the hosting provider.

Never commit:

```text
API keys
passwords
database credentials
private tokens
encryption keys
```

---

# 🧪 Testing

Test the system using a clear traffic image containing:

- Multiple vehicles
- Visible license plates
- Different vehicle types
- Different lighting conditions

For best OCR results:

- Use high-resolution images
- Keep plates reasonably visible
- Avoid extreme angles
- Avoid severe motion blur
- Avoid heavy occlusion

---

# ⚠️ Current Limitations

### 1. License plate detection

The dedicated YOLO plate detector is significantly better than generic contour-based detection, but accuracy still depends on:

- Image resolution
- Camera angle
- Lighting
- Plate size
- Occlusion

### 2. OCR

EasyOCR can make mistakes with:

```text
O ↔ 0
I ↔ 1
S ↔ 5
B ↔ 8
```

The application applies normalization and validation, but OCR should still be treated as probabilistic.

### 3. Helmet detection

The current helmet result is a heuristic.

A dedicated helmet model should be added before claiming production-grade helmet violation detection.

### 4. Serverless deployment

The AI inference stack is heavy.

For continuous CCTV/video processing, use persistent compute rather than serverless functions.

---

# 🔮 Future Improvements

- Dedicated helmet detection model
- Red-light crossing line detection
- Speed violation detection
- Multi-camera support
- Real-time CCTV streams
- Vehicle tracking across frames
- PostgreSQL violation database
- Cloud evidence storage
- Automatic challan generation
- SMS/email notifications
- Police/admin dashboard
- Role-based authentication
- Real-time WebSocket monitoring
- GPU inference
- License plate database
- Duplicate violation prevention
- Advanced Indian plate validation

---

# 🎯 Project Objective

The goal of Smart Traffic Violation is to demonstrate how computer vision and OCR can automate traffic monitoring.

Instead of manually reviewing every frame:

```text
Traffic Camera
      ↓
AI Detection
      ↓
Vehicle Identification
      ↓
License Plate Recognition
      ↓
Violation Analysis
      ↓
Evidence
      ↓
Digital Record
```

This can reduce manual monitoring effort and provide structured traffic-violation data.

---

# 👨‍💻 Author

**Annam Pranav**

GitHub:

https://github.com/AnnamPranav

Project:

**Smart Traffic Violation — ANPR & OCR**

---

# 📄 License

This project is intended for educational, research, and demonstration purposes.

Before using it in a real traffic-enforcement environment, validate model accuracy, privacy requirements, legal requirements, evidence standards, and applicable local regulations.
