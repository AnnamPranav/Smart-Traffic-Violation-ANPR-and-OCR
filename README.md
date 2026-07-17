# AI License Plate Intelligence System

Real-Time Automatic Number Plate Recognition (ANPR) using YOLOv8, EasyOCR, and OpenCV.

---

# Overview

The AI License Plate Intelligence System is a real-time Automatic Number Plate Recognition (ANPR) application that detects vehicles, identifies license plates, extracts plate text using OCR, and tracks vehicles across video frames.

The project combines deep learning and computer vision technologies to provide accurate license plate recognition for surveillance, smart transportation, parking management, toll systems, and traffic monitoring. :contentReference[oaicite:0]{index=0}

---

# Features

- Real-time vehicle detection
- Automatic license plate detection
- OCR-based license plate recognition
- Vehicle tracking across frames
- Live camera and video file support
- Interactive graphical user interface
- Real-time performance dashboard
- Automatic CSV report generation
- Output video generation
- Automatic screenshot capture
- GPU acceleration support
- Automatic model download

---

# Technology Stack

- Python
- YOLOv8
- OpenCV
- EasyOCR
- NumPy
- Pandas
- Pillow
- Tkinter
- Ultralytics
- Colorama
- tqdm

---

# Project Structure

```
AI-License-Plate-System/
│
├── output_anpr/
│   ├── output.mp4
│   ├── plates.csv
│   └── screenshots/
│
├── license_plate_detector.pt
├── main.py
├── requirements.txt
└── README.md
```

---

# System Architecture

```
Camera / Video
      │
      ▼
Vehicle Detection (YOLOv8)
      │
      ▼
Vehicle Tracking
      │
      ▼
License Plate Detection
      │
      ▼
OCR (EasyOCR)
      │
      ▼
License Plate Extraction
      │
      ▼
CSV Logging
      │
      ▼
Live Dashboard & Output Video
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-License-Plate-System.git
```

Navigate to the project directory

```bash
cd AI-License-Plate-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

The application automatically downloads the required YOLOv8 license plate detection model if it is not available.

---

# Usage

Run using webcam

```bash
python main.py
```

Run using a video file

```bash
python main.py video.mp4
```

Run with custom parameters

```bash
python main.py video.mp4 --every 2 --ocr-recheck 45 --max-ocr 3
```

---

# Output

The application generates:

- Annotated output video
- CSV file containing detected license plates
- Vehicle tracking information
- Automatic screenshots
- Live dashboard with statistics

---

# Performance

- High-speed real-time detection
- Multi-vehicle tracking
- Accurate OCR recognition
- GPU and CPU support
- Confidence-based recognition
- Optimized inference pipeline

---

# Applications

- Smart Traffic Management
- Toll Plaza Automation
- Parking Management Systems
- Vehicle Access Control
- Smart City Infrastructure
- Security Surveillance
- Campus Vehicle Monitoring
- Law Enforcement

---

# Future Enhancements

- Vehicle speed estimation
- Face recognition integration
- Automatic violation detection
- Cloud database integration
- REST API support
- Mobile application
- Multi-camera monitoring
- AI analytics dashboard

---

# Developer

**Annam Pranav Reddy**

B.Tech in Computer Science Engineering

**Areas of Interest**

- Artificial Intelligence
- Computer Vision
- Machine Learning
- Robotics
- Intelligent Transportation Systems
- Smart Surveillance

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

This project is built using the following open-source technologies:

- Ultralytics YOLOv8
- OpenCV
- EasyOCR
- NumPy
- Pandas
- Pillow
- Tkinter
```
