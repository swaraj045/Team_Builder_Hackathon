from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base


class Receiver(Base):
    __tablename__ = "receivers"

    id = Column(Integer, primary_key=True, index=True)

    # Receiver UPI ID (example: fraud@upi)
    upi_id = Column(String(100), unique=True, index=True, nullable=False)

    # Trust Score (0 - 100)
    trust_score = Column(Integer, default=100)

    # Total fraud complaints reported
    fraud_complaints = Column(Integer, default=0)

    # Whether receiver is blacklisted
    is_blacklisted = Column(Boolean, default=False)

    # Risk category (LOW, MEDIUM, HIGH)
    risk_level = Column(String(20), default="LOW")

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)