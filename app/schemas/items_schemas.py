from pydantic import BaseModel
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime
    updated_at: datetime

class ItemsListResponse(BaseModel):
    items: list[ItemResponse]