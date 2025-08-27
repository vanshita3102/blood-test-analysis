from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    """Base user data that can be shared between requests and responses"""
    email: Optional[str] = None
    name: Optional[str] = None

class UserCreate(UserBase):
    """Data required when creating a new user"""
    pass

class User(UserBase):
    """User data that we send back in responses"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy models

class AnalysisResultBase(BaseModel):
    """Base analysis result data"""
    filename: Optional[str] = None
    hemoglobin: Optional[float] = None
    wbc: Optional[float] = None
    rbc: Optional[float] = None
    platelets: Optional[float] = None
    analysis_text: Optional[str] = None
    status: str = "completed"

class AnalysisResultCreate(AnalysisResultBase):
    """Data required when creating a new analysis result"""
    user_id: Optional[int] = None

class AnalysisResult(AnalysisResultBase):
    """Analysis result data that we send back in responses"""
    id: int
    user_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

class AnalysisResultWithUser(AnalysisResult):
    """Analysis result that includes user information"""
    user: Optional[User] = None
