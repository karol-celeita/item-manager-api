from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import items_services
from schemas.items_schemas import ItemCreate, ItemResponse, ItemsListResponse

router = APIRouter(prefix="/api/v1", tags=["items"])

@router.post("/create", response_model=ItemResponse)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return items_services.create_item(db,item)
