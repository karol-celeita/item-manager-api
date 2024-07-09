from sqlalchemy.orm import Session
from models.items import Item
from schemas.items_schemas import ItemCreate
from sqlalchemy.exc import SQLAlchemyError

def create_item(db: Session, item: ItemCreate) -> Item:
    """
    Create a new item in the database.

    Args:
        db (Session): SQLAlchemy database session.
        item (ItemCreate): Item creation schema containing `name` and `price` of the item.

    Returns:
        Item: The newly created `Item` object.

    Raises:
        SQLAlchemyError: If there is an error committing the transaction.

    """
    db_item = Item(name=item.name, price=item.price)
    db.add(db_item)
    
    try:
        db.commit()
        db.refresh(db_item)
        return db_item
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError(f"Failed to create item: {str(e)}")

def get_items(db: Session, skip: int, limit:int) -> list[Item]:
    """
    Retrieve a list of items from the database with pagination.

    Args:
        db (Session): SQLAlchemy database session.
        skip (int, optional): The number of items to skip before starting to collect the result set. Defaults to 0.
        limit (int, optional): The maximum number of items to return. Defaults to 10.

    Returns:
        list[Item]: A list of `Item` objects retrieved from the database.
    """
    return db.query(Item).offset(skip).limit(limit).all()