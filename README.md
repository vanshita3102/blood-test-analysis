Blood Test Analyser - Fixed (Safe Mock)

This repository is a fixed, working version of the original debugging assignment.
It removes unsafe instructions and CrewAI dependencies, replacing them with a deterministic, mock pipeline that extracts text from PDFs and performs a simple rule-based analysis of common blood metrics.

Additionally, a Redis Queue (RQ) worker model is integrated to handle background tasks and concurrent requests.

🐞 Bugs Found & Fixes

Issue: Original code depended on unsafe/unsupported libraries (CrewAI).
Fix: Replaced with safe, rule-based text extraction + mock analysis.

Issue: Jobs were executed directly in the main process.
Fix: Integrated RQ (Redis Queue) and added a worker.py script for background job processing.

Issue: Project lacked reproducibility.
Fix: Added requirements.txt and clear setup instructions.

⚡ Quick Start
1. Clone and Setup
git clone <your-repo-link>
cd debug-assignment-fixed
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Start Redis

Make sure Redis is installed and running. On macOS (with Homebrew):

brew install redis
brew services start redis

3. Run the API
uvicorn main:app --reload


The API will be available at:
👉 http://127.0.0.1:8000/docs

4. Start the Worker

Open another terminal in the same project folder and run:

source .venv/bin/activate
rq worker

📌 API Documentation
POST /analyze

Analyzes a blood test PDF.

Request:
Multipart form with optional file (PDF).

Response:
JSON with extracted metrics and simple analysis.

Example:

curl -X POST "http://127.0.0.1:8000/analyze" \
-F "file=@data/sample.pdf"


Response:

{
  "hemoglobin": "13.5",
  "cholesterol": "190",
  "analysis": "All values within normal range."
}

🛠 Bonus: Queue Worker Model

This project uses RQ (Redis Queue) for handling background jobs.

Flow:

API receives a request.

Task is queued in Redis.

Worker (worker.py) picks up the job.

Result is stored and returned.

You can see queued/finished jobs using:

rq info

🚀 Example: Enqueueing a Job

In a Python shell (with your virtualenv activated):

from redis import Redis
from rq import Queue
from tasks import small   # example task function

# connect to Redis
redis_conn = Redis()
q = Queue(connection=redis_conn)

# enqueue a job
job = q.enqueue(small, 5)

print("Job ID:", job.id)
print("Status:", job.get_status())


Then, in a separate terminal where the worker is running (rq worker), you’ll see the job being picked up and executed.

Check the result later:

print("Result:", job.result)  # should print 6

📦 Requirements

The main dependencies are listed in requirements.txt:

fastapi
uvicorn
redis
rq
python-dateutil
pytz


Install all at once:

pip install -r requirements.txt

⚠️ Notes

This is a mock, non-medical analysis for debugging/demo purposes only.

Do not use this for real medical decisions.
