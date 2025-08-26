from fastapi import FastAPI, File, UploadFile, HTTPException, Form
import os
import uuid
from typing import Optional

from tools import read_pdf_text, parse_metrics_from_text, analyze_metrics

app = FastAPI(title="Blood Test Report Analyser (Safe Mock)")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
OUTPUTS_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/analyze")
async def analyze(file: Optional[UploadFile] = File(None), async_mode: bool = Form(False)):
    '''
    Upload a blood test PDF (multipart/form-data).
    If no file is provided, the server will analyze data/sample.pdf.
    '''
    # Save uploaded file
    if file is not None:
        filename = f"upload_{uuid.uuid4().hex}_{file.filename}"
        file_path = os.path.join(DATA_DIR, filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
    else:
        file_path = os.path.join(DATA_DIR, "sample.pdf")
        if not os.path.exists(file_path):
            raise HTTPException(status_code=400, detail="No file uploaded and sample.pdf not found.")

    try:
        text = read_pdf_text(file_path)
        metrics = parse_metrics_from_text(text)
        result = analyze_metrics(metrics)
        # persist result to outputs
        out_path = os.path.join(OUTPUTS_DIR, f"result_{uuid.uuid4().hex}.txt")
        with open(out_path, "w", encoding="utf-8") as fo:
            fo.write("Parsed Metrics:\n")
            fo.write(str(metrics) + "\n\n")
            fo.write("Analysis:\n")
            fo.write(result)
        return {"status":"success", "metrics": metrics, "analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))