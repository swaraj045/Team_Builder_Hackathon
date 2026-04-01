from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database.db_connection import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    sender = Column(String)
    receiver = Column(String)
    amount = Column(Float)
    status = Column(String)
    risk_score = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())