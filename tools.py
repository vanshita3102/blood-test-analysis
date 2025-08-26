import re
from typing import Dict
from PyPDF2 import PdfReader

def read_pdf_text(path: str) -> str:
    """Extract text from a PDF using PyPDF2."""
    reader = PdfReader(path)
    texts = []
    for page in reader.pages:
        texts.append(page.extract_text() or "")
    return "\n".join(texts)

def parse_metrics_from_text(text: str) -> Dict[str, float]:
    """Very small parser: look for common blood metrics and numbers near them."""
    metrics = {}
    # patterns for common tests
    patterns = {
        'hemoglobin': r'(hemoglobin|hb)[:\s]*([0-9]+\.?[0-9]*)',
        'wbc': r'(wbc|white blood cells|white blood cell count)[:\s]*([0-9]+\.?[0-9]*)',
        'rbc': r'(rbc|red blood cells)[:\s]*([0-9]+\.?[0-9]*)',
        'platelets': r'(platelets?)[:\s]*([0-9]+\,?[0-9]*)'
    }
    lower = text.lower()
    for key, pat in patterns.items():
        m = re.search(pat, lower)
        if m:
            num = m.group(2).replace(',','')
            try:
                metrics[key] = float(num)
            except:
                pass
    return metrics

def analyze_metrics(metrics: Dict[str, float]) -> str:
    """Simple rule-based analysis (mock, not medical advice)."""
    if not metrics:
        return "No recognizable metrics found in the report. This is a mock analysis."
    notes = []
    hb = metrics.get('hemoglobin')
    if hb is not None:
        if hb < 12:
            notes.append(f"Hemoglobin ({hb}) is low → possible anemia (mock). Recommend clinical review.")
        elif hb > 17.5:
            notes.append(f"Hemoglobin ({hb}) is high → may indicate dehydration or other factors (mock). Recommend review.")
        else:
            notes.append(f"Hemoglobin ({hb}) is within typical adult ranges (mock).")

    wbc = metrics.get('wbc')
    if wbc is not None:
        # many labs report WBC in 10^9/L; here we just use thresholds heuristically
        if wbc < 4:
            notes.append(f"WBC ({wbc}) is low → possible leukopenia (mock). Recommend clinical review.")
        elif wbc > 11:
            notes.append(f"WBC ({wbc}) is high → possible infection or inflammation (mock). Recommend review.")
        else:
            notes.append(f"WBC ({wbc}) is within typical ranges (mock).")

    plate = metrics.get('platelets')
    if plate is not None:
        if plate < 150:
            notes.append(f"Platelets ({plate}) are low → possible thrombocytopenia (mock). Recommend review.")
        elif plate > 450:
            notes.append(f"Platelets ({plate}) are high ({plate}) → may indicate reactive thrombocytosis (mock). Recommend review.")
        else:
            notes.append(f"Platelets ({plate}) are within typical ranges (mock).")

    return "\n".join(notes)