from sqlalchemy.orm import Session
from repositories import item_repository
from schemas.items_schemas import ItemCreate, ItemResponse, ItemsListResponse

def create_item(db: Session, item: ItemCreate) -> ItemResponse:
    db_item = item_repository.create_item(db, item)
    return ItemResponse(
        id=db_item.id, 
        name=db_item.name, 
        price=db_item.price, 
        created_at=db_item.created_at, 
        updated_at=db_item.updated_at
    )
