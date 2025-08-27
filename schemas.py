from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class AnalysisResultBase(BaseModel):
    filename: Optional[str] = None
    hemoglobin: Optional[float] = None
    wbc: Optional[float] = None
    rbc: Optional[float] = None
    platelets: Optional[float] = None
    analysis_text: Optional[str] = None
    status: str = "completed"

class AnalysisResultCreate(AnalysisResultBase):
    user_id: Optional[int] = None

class AnalysisResult(AnalysisResultBase):
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class AnalysisResultWithUser(AnalysisResult):
    user: Optional[User] = None
