from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime, timezone
from database import Base

class Item(Base):
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, server_default='0',nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))