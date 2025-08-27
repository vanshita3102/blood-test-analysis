# 🧪 Blood Test Analyser — Fixed & Enhanced  

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=flat&logo=redis&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=flat&logo=sqlite&logoColor=white)

A **safe, fixed, and enhanced** version of the original debugging assignment.
Analyzes **blood test PDFs**, runs **rule-based analysis**, supports **background jobs via Redis Queue (RQ)**, and includes **complete database integration** with user management and persistent data storage.

## ✨ Features
- ✅ Fixed bugs from the original assignment
- ✅ Rule-based mock blood test analysis (safe, non-medical)  
- ✅ Background task processing with Redis Queue (RQ)
- ✅ **Database integration with user management and data persistence**
- ✅ Clear API built with FastAPI
- ✅ **Enhanced API endpoints for querying analysis history**
- ✅ Simple setup & usage

## 🎉 Database Integration in Action
### Professional API Documentation
<img width="500" alt="Interactive Swagger UI Documentation" src="https://github.com/user-attachments/assets/79f1047e-9644-419d-ba5b-7f07e3e05d13" />

*Auto-generated interactive API documentation showing all database endpoints*

### Database Integration Success
<img width="400" alt="Database Tables Created Successfully" src="https://github.com/user-attachments/assets/daf3c8c8-efa9-4ae9-a50b-d9b9d3371051" />

*Server startup showing successful database table creation*



  
## 🐞 Bugs Fixed
1. **Unsafe CrewAI dependencies** → replaced with deterministic mock logic
2. **Direct PDF parsing issues** → fallback to data/sample.pdf included  
3. **Blocking requests** → introduced Redis Queue (RQ) for async job handling
4. **File-based storage limitations** → implemented database integration for persistent data

## 🚀 Quick Setup
```bash
# 1️⃣ Clone & Setup Environment
git clone <your-repo-link>
cd debug-assignment-fixed
python3 -m venv .venv
source .venv/bin/activate

###Install all dependencies (including database packages)
pip install -r requirements.txt

###Or install manually:
pip install fastapi uvicorn python-dotenv PyPDF2 sqlalchemy alembic python-multipart redis rq

# 2️⃣ Run Redis (local)
redis-server

# 3️⃣ Or run Redis with Docker
docker run -p 6379:6379 redis

# 4️⃣ Start the Worker
rq worker

# 5️⃣ Run the API
uvicorn main:app --reload

```

**✅ You should see:** `🎉 Database tables created successfully!`

## 📌 Usage & API

You can analyze a blood test report by uploading a PDF with optional user information.
If no file is uploaded, the included data/sample.pdf will be used.

⚠️ Note: This analysis is mock & non-medical — for debugging only.

### Core Endpoints

#### Analyze Blood Test (Enhanced with Database)

```bash
POST /analyze
Content-Type: multipart/form-data
```
**Parameters:**
- `file` (optional): Blood test PDF file
- `user_email` (optional): User's email address
- `user_name` (optional): User's full name

#### Database Query Endpoints
```bash
GET /users # List all users
GET /analyses # List all analysis results
GET /users/{user_id}/analyses # Get analyses for specific user
GET /analyses/{analysis_id} # Get specific analysis result
GET /health # Health check with database status
```
### Example Request

#### Basic Analysis (No User Data)
```bash
curl -X POST "http://127.0.0.1:8000/analyze"
-F "file=@data/sample.pdf"
```
#### Enhanced Analysis with User Data
```bash
curl -X POST "http://127.0.0.1:8000/analyze"
-F "file=@data/sample.pdf"
-F "user_email=john@example.com"
-F "user_name=John Doe"
```

#### Query Database
```bash
Get all users
curl http://127.0.0.1:8000/users

Get all analysis results with user information
curl http://127.0.0.1:8000/analyses

Get analyses for specific user (replace 1 with actual user ID)
curl http://127.0.0.1:8000/users/1/analyses
```

### Example Response (Database Enhanced)

**New Structured Response:**
```bash
{
"id": 1,
"user_id": 1,
"filename": "upload_abc123_blood_test.pdf",
"file_path": "/path/to/file",
"hemoglobin": null,
"wbc": null,
"rbc": null,
"platelets": null,
"analysis_text": "No recognizable metrics found in the report. This is a mock analysis.",
"status": "completed",
"created_at": "2025-08-27T08:33:00.123456"
}
```

**Users Endpoint Response:**
```bash
[
{
"id": 1,
"email": "john@example.com",
"name": "John Doe",
"created_at": "2025-08-27T08:30:00.123456"
}
]
```

### Interactive API Documentation

Visit these URLs when your server is running:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📂 Project Structure
```plaintext
debug-assignment-fixed/
│── main.py # FastAPI app with database integration
│── models.py # Database table definitions (Users, AnalysisResults)
│── database.py # Database connection and session management
│── schemas.py # Pydantic models for data validation
│── tools.py # PDF parsing and analysis utilities
│── tasks.py # Background task definitions (RQ)
│── worker.py # Worker setup (RQ)
│── requirements.txt # All dependencies including database packages
│── blood_test_analysis.db # SQLite database (auto-created)
│── data/
│ └── sample.pdf # Sample blood test PDF
│── outputs/ # Legacy output directory (now uses database)
│── README.md
```

## 🎉 Database Integration Features

### Database Schema
- **Users Table**: Stores user information (id, email, name, created_at)
- **Analysis Results Table**: Stores blood test analysis data with foreign key to users
- **Relationships**: One user can have many analysis results

### Key Benefits
✅ **Persistent Storage**: Data survives server restarts  
✅ **User Management**: Track who uploads files  
✅ **Query Capabilities**: Rich API endpoints for data retrieval  
✅ **Structured Data**: Organized tables with relationships  
✅ **Audit Trail**: Timestamps and user tracking  

### Database Technologies Used
- **SQLAlchemy**: Python SQL toolkit and ORM
- **SQLite**: Lightweight, file-based database
- **Alembic**: Database migration tool (for future schema changes)
- **Pydantic**: Data validation and serialization

## 🏆 Bonus Features

✅ **Queue Worker Model**: Redis Queue for concurrent requests  
✅ **Database Integration**: Complete user management and data persistence  

### Background Processing (Redis Queue)
- Handles concurrent requests efficiently
- Prevents blocking on long-running analysis tasks
- Scalable worker-based architecture

### Database Integration
- User registration and management
- Persistent analysis result storage  
- Rich query API endpoints
- Structured data relationships

## 🧪 Testing Your Setup
1. Test health check
curl http://127.0.0.1:8000/health

Expected: {"ok": true, "database": "connected"}
2. Test analysis with user data
curl -X POST "http://127.0.0.1:8000/analyze"
-F "user_email=test@example.com"
-F "user_name=Test User"

3. Verify user was created
curl http://127.0.0.1:8000/users

4. Check analysis results
curl http://127.0.0.1:8000/analyses

## 🔧 Dependencies

Core FastAPI
fastapi
uvicorn
python-dotenv
PyPDF2

Database Integration
sqlalchemy>=2.0.0
alembic
python-multipart

Background Processing
redis
rq

## ⚠️ Disclaimer

This project is a mock analyzer for debugging purposes only.
It does not provide medical advice, diagnostics, or treatment recommendations.

All analysis results are generated using rule-based mock logic and should not be used for actual medical decision-making.

## 🚀 Development Notes

- Database file (`blood_test_analysis.db`) is auto-created on first run
- SQL queries are logged to console when `echo=True` in database.py
- Use the interactive API docs at `/docs` for easy testing
- Background workers are optional but recommended for production use








