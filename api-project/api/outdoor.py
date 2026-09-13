from fastapi import APIRouter

api_outdoor = APIRouter()

@api_outdoor.get("/")
def read_root():
    return {"message": "Hello, World!"}

@api_outdoor.get("/items")
def read_items():
    return {"message": "Items!"}

@api_outdoor.post("/items")
def create_item(item: str): 
    return {"message": "Item created: " + item}

@api_outdoor.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    return {"message": "Item updated: " + item}

@api_outdoor.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted: " + item_id}