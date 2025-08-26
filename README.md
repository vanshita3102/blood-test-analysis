# Blood Test Analyser - Fixed (Safe Mock)

This repository is a fixed, safe version of the original debugging assignment.
It removes unsafe instructions and CrewAI dependencies and replaces them with
a deterministic, mock pipeline that extracts text from PDFs and performs a
simple rule-based analysis of common blood metrics.

## Quick start

1. Create virtual env and activate:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the API:
```bash
uvicorn main:app --reload
```

3. Use the `/analyze` endpoint with a PDF file upload (multipart form).
If no file is provided, the included `data/sample.pdf` will be used.

## Notes
- This is a mock, non-medical analysis for debugging purposes only.
- The code intentionally avoids using external LLM libraries or CrewAI.