from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Database URL - using SQLite for simplicity
# This creates a file called 'blood_test_analysis.db' in your project folder
DATABASE_URL = "sqlite:///./blood_test_analysis.db"

# Create engine
# echo=True means it will print all SQL queries (helpful for learning!)
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Remove this in production
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_database():
    """
    Dependency function that provides database sessions to our API endpoints

     This is like borrowing a book from the library:
    1. Get a session (check out the book)
    2. Use it to read/write data
    3. Close it when done (return the book)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
