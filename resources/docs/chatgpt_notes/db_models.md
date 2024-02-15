## (Q1) Some examples of Fast API-based CRUD operations, which use Pydantic models in examples!

Sure, here are some examples of FastAPI-based CRUD operations using Pydantic models:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define Pydantic model
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# In-memory database
items_db = []
```


**Create Operation:**

```python
# Create operation
@app.post("/items/")
async def create_item(item: Item):
    items_db.append(item)
    return item
```

**Read Operation:**

```python
# Read operation
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]
```

**Update Operation:**

```python
# Update operation
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item
```

**Delete Operation:**

```python
# Delete operation
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "deleted_item": deleted_item}
```

These examples demonstrate how to perform basic CRUD operations using FastAPI and Pydantic models. The Item model is used to define the structure of the data being sent to and received from the API endpoints. The operations handle requests to create, read, update, and delete items from an in-memory database.
