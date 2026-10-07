# Smart Traffic Violation + ANPR

A full-stack traffic intelligence application combining:

- YOLOv8 vehicle detection
- Dedicated YOLO license-plate detection
- EasyOCR license-plate recognition
- Traffic signal violation logic
- Evidence image generation
- Detection history
- Browser frontend
- REST API

The dedicated plate detector is based on the public YOLOv8 license-plate model used by the Automatic-License-Plate-Recognition-using-YOLOv8 project. The source project documents the use of a dedicated plate detector followed by OCR. The model is downloaded at setup time rather than committed into this repository.

## Architecture

Browser
→ Flask REST API
→ Vehicle detector
→ License-plate detector
→ Plate OCR
→ Violation engine
→ Evidence + JSON history

## Local setup

Use Python 3.10 or 3.11.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_models.py
python backend/app.py
```

Open:

http://localhost:5000

The first AI startup can take time because YOLO/EasyOCR models are loaded.

## API

### Health

GET `/api/health`

### Analyze image

POST `/api/detect`

Multipart:
- `image`
- `signal=RED|GREEN`

### History

GET `/api/history`

## What is actually detected

The application does NOT generate fake/random plate numbers.

It performs:

1. Vehicle detection
2. Dedicated license-plate detection
3. Plate crop extraction
4. OCR preprocessing
5. EasyOCR recognition
6. Registration-pattern validation/scoring
7. Violation evaluation
8. Evidence storage

## Important limitation

The current `Possible No Helmet` rule is still a heuristic because the original project does not include a dedicated helmet-detection model. It must not be described as confirmed helmet detection until such a model is added.

## Deployment

### Backend

Recommended for the AI backend: Render/Railway or another persistent Python service. The included `render.yaml` and `Procfile` are ready for that style of deployment.

### Frontend

The `frontend/` folder is static and can be deployed to Vercel. If deployed separately, change the frontend fetch calls from `/api/...` to the deployed backend URL, ideally through an environment/config value.

### Why not Vercel for the AI backend?

YOLO + PyTorch + EasyOCR are heavy Python dependencies and model files. A persistent Python service is much more suitable for this workload than a serverless function. Vercel is best used here for the browser frontend.

## Model licensing / provenance

The dedicated plate detector is downloaded from:
https://github.com/Muhammad-Zeerak-Khan/Automatic-License-Plate-Recognition-using-YOLOv8

That repository states the project is MIT licensed and uses a YOLOv8 vehicle model, a dedicated license-plate detector, and EasyOCR. Review the upstream model/license terms before commercial use.
