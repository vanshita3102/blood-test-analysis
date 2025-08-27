from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Depends
from sqlalchemy.orm import Session
import os
import uuid
from typing import Optional, List

# Import database components
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
    Base.metadata.create_all(bind=engine)
    print("🎉 Database tables created successfully!")

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
    Analyze blood test PDF with database storage
    """
    
    # Handle user creation/retrieval
    user = None
    if user_email:
        user = db.query(User).filter(User.email == user_email).first()
        if not user:
            user = User(email=user_email, name=user_name)
            db.add(user)
            db.commit()
            db.refresh(user)
            print(f"✅ Created new user: {user.email}")
    
    # Handle file
    if file is not None:
        filename = f"upload_{uuid.uuid4().hex}_{file.filename}"
        file_path = os.path.join(DATA_DIR, filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
    else:
        filename = "sample.pdf"
        file_path = os.path.join(DATA_DIR, "sample.pdf")
        if not os.path.exists(file_path):
            raise HTTPException(status_code=400, detail="No file uploaded and sample.pdf not found.")

    try:
        # Perform analysis
        text = read_pdf_text(file_path)
        metrics = parse_metrics_from_text(text)
        analysis = analyze_metrics(metrics)
        
        # Save to database
        analysis_result = AnalysisResult(
            user_id=user.id if user else None,
            filename=filename,
            file_path=file_path,
            hemoglobin=metrics.get('hemoglobin'),
            wbc=metrics.get('wbc'),
            rbc=metrics.get('rbc'),
            platelets=metrics.get('platelets'),
            analysis_text=analysis,
            status="completed"
        )
        
        db.add(analysis_result)
        db.commit()
        db.refresh(analysis_result)
        
        print(f"💾 Analysis saved to database with ID: {analysis_result.id}")
        return analysis_result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# New database endpoints
@app.get("/users", response_model=List[UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_database)):
    """Get all users"""
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/analyses", response_model=List[AnalysisResultWithUser])
def get_all_analyses(skip: int = 0, limit: int = 100, db: Session = Depends(get_database)):
    """Get all analysis results"""
    analyses = db.query(AnalysisResult).offset(skip).limit(limit).all()
    return analyses

@app.get("/users/{user_id}/analyses", response_model=List[AnalysisResultSchema])
def get_user_analyses(user_id: int, db: Session = Depends(get_database)):
    """Get analyses for specific user"""
    analyses = db.query(AnalysisResult).filter(AnalysisResult.user_id == user_id).all()
    return analyses

@app.get("/analyses/{analysis_id}", response_model=AnalysisResultWithUser)
def get_analysis(analysis_id: int, db: Session = Depends(get_database)):
    """Get specific analysis"""
    analysis = db.query(AnalysisResult).filter(AnalysisResult.id == analysis_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return analysis
