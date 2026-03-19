from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()


@router.get("")
async def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint that verifies database connectivity
    """
    try:
        # Test database connection
        db.execute("SELECT 1")
        return {
            "status": "healthy",
            "database": "connected",
            "message": "Service is running correctly",
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "message": f"Database connection failed: {str(e)}",
        }
