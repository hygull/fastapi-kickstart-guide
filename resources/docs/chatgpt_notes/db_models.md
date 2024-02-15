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


## (Q2) Please represent this using DB!

Sure, let's modify the examples to use a database instead of an in-memory list. We'll use SQLAlchemy to interact with the database. Here's how you can represent the CRUD operations using a database:

Set up SQLAlchemy and Database Models:

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    tax = Column(Float, nullable=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```


**Create Operation:**

```python
# Create operation
def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

**Read Operation:**

```python
# Read operation
def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()
```

**Update Operation:**

```python
# Update operation
def update_item(db: Session, item_id: int, item_update: ItemUpdate):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        for key, value in item_update.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item
```

**Delete Operation:**

```python
# Delete operation
def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
```

In these examples, we define SQLAlchemy models for the Item table and create the corresponding database tables. Then, we implement CRUD operations that interact with the database using SQLAlchemy's ORM. These operations take a database session (db: Session) as a parameter to execute queries and manipulate data in the database.
