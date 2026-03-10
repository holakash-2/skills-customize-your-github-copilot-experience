from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define your data model here
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

# In-memory storage for items
items_db = []

# TODO: Implement your routes here
# - GET /items - retrieve all items
# - GET /items/{item_id} - retrieve a specific item
# - POST /items - create a new item
# - PUT /items/{item_id} - update an item
# - DELETE /items/{item_id} - delete an item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
