from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.crud import item as item_crud

router = APIRouter()


@router.get("", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve items.
    """
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get item by ID.
    """
    item = item_crud.get_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create new item.
    """
    return item_crud.create_item(db=db, item=item)


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    """
    Update an item.
    """
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_crud.update_item(db=db, item_id=item_id, item=item)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item.
    """
    item = item_crud.get_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item_crud.delete_item(db=db, item_id=item_id)
    return {"message": "Item deleted successfully"}
