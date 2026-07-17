# License Plate Recognition System

Real-Time Automatic Number Plate Recognition (ANPR) using YOLOv8, EasyOCR, and OpenCV.

---

## Overview

The License Plate Recognition System is a real-time Automatic Number Plate Recognition (ANPR) application that detects vehicles, identifies license plates, extracts plate text using Optical Character Recognition (OCR), and tracks vehicles across video frames.

The system combines deep learning, computer vision, and OCR technologies to deliver accurate and efficient license plate recognition for intelligent transportation, surveillance, parking management, toll collection, and traffic monitoring.

---

## Features

- Real-time vehicle detection
- Automatic license plate detection
- OCR-based license plate recognition
- Multi-vehicle tracking
- Live webcam and video file support
- Interactive graphical user interface
- Real-time system dashboard
- Automatic CSV report generation
- Output video generation
- Automatic screenshot capture
- GPU acceleration support
- Automatic model download
- Confidence-based recognition
- Optimized inference pipeline

---

## Technology Stack

- Python
- YOLOv8
- OpenCV
- EasyOCR
- NumPy
- Pandas

---

## Project Structure

```text
License-Plate-Recognition-System/
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

## System Architecture

```text
Input Video / Webcam
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
Image Preprocessing
        │
        ▼
OCR Recognition (EasyOCR)
        │
        ▼
Plate Text Extraction
        │
        ▼
CSV Logging & Database
        │
        ▼
Dashboard & Output Video
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/License-Plate-Recognition-System.git
```

### Navigate to the project directory

```bash
cd License-Plate-Recognition-System
```

### Install the required dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

The application automatically downloads the required YOLOv8 license plate detection model if it is not already available.

---

## Usage

### Webcam

```bash
python main.py
```

### Video File

```bash
python main.py video.mp4
```

### Custom Parameters

```bash
python main.py video.mp4 --every 2 --ocr-recheck 45 --max-ocr 3
```

---

## Output

The application automatically generates:

- Annotated output video
- CSV file containing recognized license plates
- Vehicle tracking information
- Automatic screenshots
- Real-time dashboard statistics

---

## Performance

- High-speed real-time inference
- Accurate vehicle detection
- Reliable license plate localization
- OCR-based text extraction
- Multi-object tracking
- GPU and CPU compatibility
- Confidence-based recognition
- Optimized processing pipeline

---

## Applications

- Intelligent Traffic Management
- Smart Parking Systems
- Toll Collection Automation
- Campus Vehicle Monitoring
- Residential Security
- Law Enforcement
- Smart City Infrastructure
- Vehicle Access Control
- Industrial Security
- Transportation Analytics

---

## Future Enhancements

- Vehicle speed estimation
- Automatic violation detection
- Face recognition integration
- Cloud database support
- REST API integration
- Mobile application
- Multi-camera monitoring
- Web dashboard
- AI analytics
- License plate database search

---

## Requirements

- Python 3.10 or later
- Webcam or CCTV camera (optional)
- CUDA-enabled GPU (optional)
- Windows, Linux, or macOS

---
## Acknowledgements

This project is developed using the following open-source technologies:

- Ultralytics YOLOv8
- OpenCV
- EasyOCR
- NumPy
- Pandas

---

## License

This project is licensed under the MIT License.

---

## Developer

**Annam Pranav Reddy**
