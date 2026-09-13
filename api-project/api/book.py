from fastapi import APIRouter

api_book = APIRouter()

@api_book.get("/")
def read_root():
    return {"message": "Hello, World!"}

@api_book.get("/items")
def read_items():
    return {"message": "Items!"}

@api_book.post("/items")
def create_item(item: str):
    return {"message": "Item created: " + item}

@api_book.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    return {"message": "Item updated: " + item}

@api_book.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted: " + item_id}

