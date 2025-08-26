# 🧪 Blood Test Analyser - Fixed & Enhanced

A **fixed, safe, and enhanced** version of the original debugging assignment.  
This project analyzes blood test reports from PDFs, performs a simple rule-based analysis of common blood metrics, and now supports **background job processing with Redis Queue (RQ)**.  

---

## ✨ Features
- ✅ Fixed bugs from the original assignment  
- ✅ Rule-based mock blood test analysis (safe, non-medical)  
- ✅ Background task processing with **Redis Queue (RQ)**  
- ✅ Clear API with FastAPI  
- ✅ Easy setup and usage  

---

## 🐞 Bugs Fixed
1. **Unsafe CrewAI dependencies** → Replaced with deterministic mock logic.  
2. **Direct PDF parsing issues** → Added fallback to sample PDF.  
3. **Blocking requests** → Introduced Redis Queue for async job handling.  

---

## 🚀 Quick Setup

### 1. Clone & Setup Environment
```bash
git clone <your-repo-link>
cd debug-assignment-fixed
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
###2. Run Redis (make sure you have Redis installed locally or via Docker)
bash
Copy
Edit
redis-server
###3. Start the Worker
bash
Copy
Edit
rq worker
###4. Run the API
bash
Copy
Edit
uvicorn main:app --reload
###📌 Usage
Analyze Endpoint
Upload a PDF for analysis:

http
Copy
Edit
POST /analyze
Content-Type: multipart/form-data
If no file is uploaded, the included data/sample.pdf will be used.

The analysis is mock & non-medical — for debugging only.

⚙️ API Endpoints
POST /analyze
Description: Analyze a blood test PDF.

Params: file (optional, PDF file).

Response: JSON with extracted values & mock analysis.

Example Request (with file)
bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/analyze" \
-F "file=@data/sample.pdf"
Example Response
json
Copy
Edit
{
  "status": "completed",
  "results": {
    "Hemoglobin": "Normal",
    "WBC": "Slightly High",
    "Platelets": "Normal"
  },
  "notes": "This is a mock, non-medical analysis."
}
###📂 Project Structure
bash
Copy
Edit
debug-assignment-fixed/
│── main.py         # FastAPI app
│── tasks.py        # Background task definitions
│── worker.py       # Worker setup (RQ)
│── requirements.txt
│── data/sample.pdf
│── README.md
🏆 Bonus Features
✅ Queue Worker Model: Redis Queue for concurrent requests

🚧 (Optional) Database integration for storing results

⚠️ Disclaimer
This project is a mock analyzer for debugging only.
It does not provide medical advice.

