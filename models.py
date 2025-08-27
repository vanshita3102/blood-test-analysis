from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    """
    User table to store basic user information
    Think of this like a contact card for each person using our app
    """
    __tablename__ = "users"

    # Primary key - unique ID for each user
    id = Column(Integer, primary_key=True, index=True)

    # User details
    email = Column(String(255), unique=True, index=True, nullable=True)
    name = Column(String(255), nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship: One user can have many analysis results
    analyses = relationship("AnalysisResult", back_populates="user")
  
class AnalysisResult(Base):
    """
    Analysis results table to store blood test analysis data
    Each row represents one analysis of a blood test PDF
    """
    __tablename__ = "analysis_results"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Link to user (foreign key)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    # File information
    filename = Column(String(255), nullable=True)
    file_path = Column(String(500), nullable=True)

    # Blood test metrics (stored as individual columns)
    hemoglobin = Column(Float, nullable=True)
    wbc = Column(Float, nullable=True)
    rbc = Column(Float, nullable=True)
    platelets = Column(Float, nullable=True)

    # Analysis results
    analysis_text = Column(Text, nullable=True)
    status = Column(String(50), default="completed")

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship: Many results belong to one user
    user = relationship("User", back_populates="analyses")
