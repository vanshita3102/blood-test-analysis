# 🧪 Blood Test Analyser — Fixed & Enhanced  

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Redis](https://img.shields.io/badge/Redis-Queue-red?logo=redis)](https://redis.io/)

A **safe, fixed, and enhanced** version of the original debugging assignment.  
Analyzes **blood test PDFs**, runs a simple **rule-based analysis**, and supports **background jobs via Redis Queue (RQ)**.

## ✨ Features
- ✅ Fixed bugs from the original assignment
- ✅ Rule-based mock blood test analysis *(safe, non-medical)*
- ✅ Background task processing with **Redis Queue (RQ)**
- ✅ Clear API built with **FastAPI**
- ✅ Simple setup & usage

## 🐞 Bugs Fixed
1. **Unsafe CrewAI dependencies** → replaced with deterministic mock logic
2. **Direct PDF parsing issues** → fallback to `data/sample.pdf` included
3. **Blocking requests** → introduced **Redis Queue (RQ)** for async job handling

## 🚀 Quick Setup
```bash
# 1️⃣ Clone & Setup Environment
git clone <your-repo-link>
cd debug-assignment-fixed
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2️⃣ Run Redis (local)
redis-server

# 3️⃣ Or run Redis with Docker
docker run -p 6379:6379 redis

# 4️⃣ Start the Worker
rq worker

# 5️⃣ Run the API
uvicorn main:app --reload

```
## 📌 Usage & API

You can analyze a blood test report by uploading a PDF.
If no file is uploaded, the included data/sample.pdf will be used.

⚠️ Note: This analysis is mock & non-medical — for debugging only.

### Endpoint
```bash
POST /analyze
Content-Type: multipart/form-data
```

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
-F "file=@data/sample.pdf"
```

### Example Response
```json
{
  "status": "completed",
  "results": {
    "Hemoglobin": "Normal",
    "WBC": "Slightly High",
    "Platelets": "Normal"
  },
  "notes": "This is a mock, non-medical analysis."
}
```

## 📂 Project Structure
```plaintext
debug-assignment-fixed/
│── main.py         # FastAPI app
│── tasks.py        # Background task definitions
│── worker.py       # Worker setup (RQ)
│── requirements.txt
│── data/sample.pdf
│── README.md
```

## 🏆 Bonus Features
✅ Queue Worker Model: Redis Queue for concurrent requests

🚧 Optional Database Integration for storing results (future-ready)

## ⚠️ Disclaimer
This project is a mock analyzer for debugging purposes only.
It does not provide medical advice, diagnostics, or treatment recommendations.





