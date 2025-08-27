from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Depends
from sqlalchemy.orm import Session
import os
import uuid
from typing import Optional, List
from datetime import datetime

# Import our new database components
from database import get_database, engine
from models import Base, User, AnalysisResult
from schemas import (
    UserCreate, User as UserSchema, 
    AnalysisResultCreate, AnalysisResult as AnalysisResultSchema,
    AnalysisResultWithUser
)
from tools import read_pdf_text, parse_metrics_from_text, analyze_metrics

app = FastAPI(title="Blood Test Report Analyser (With Database)")

# Create database tables on startup
@app.on_event("startup")
def create_tables():
    """
    This runs when the app starts up
    It creates all our database tables if they don't exist
    """
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"ok": True, "database": "connected"}

@app.post("/analyze", response_model=AnalysisResultSchema)
async def analyze(
    file: Optional[UploadFile] = File(None), 
    user_email: Optional[str] = Form(None),
    user_name: Optional[str] = Form(None),
    db: Session = Depends(get_database)
):
    """
    Analyze a blood test PDF and save results to database

    New features:
    - Creates or finds a user based on email
    - Saves analysis results to database instead of files
    - Returns structured data
    """

 # Handle user creation/retrieval
    user = None
    if user_email:
        # Try to find existing user
        user = db.query(User).filter(User.email == user_email).first()
        if not user:
            # Create new user
            user = User(email=user_email, name=user_name)
            db.add(user)
            db.commit()
            db.refresh(user)
            print(f"Created new user: {user.email}")

    # Handl
