from sqlalchemy import Column, Integer, String, Float
from app.database.db_connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    name = Column(String)
    avg_transaction_amount = Column(Float, default=2000)
    risk_level = Column(String, default="NORMAL")