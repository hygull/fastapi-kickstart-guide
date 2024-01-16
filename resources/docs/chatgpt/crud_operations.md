## How to perform CRUD operations using FastAPI?

Performing CRUD (Create, Read, Update, Delete) operations in FastAPI involves defining routes that handle HTTP methods (GET, POST, PUT, DELETE) and using a database to interact with data. Here's a basic example using SQLAlchemy as the ORM (Object-Relational Mapping) library:

Assuming you have a model **Item** defined in a file **models.py**:

```python
# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
```

And you have a file **database.py** to set up the database:

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

Now, create a file **crud.py** to define CRUD operations:

```python
# crud.py
from sqlalchemy.orm import Session
from .models import Item

def create_item(db: Session, item: Item):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, new_item: Item):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    for key, value in new_item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
```

Now, create a FastAPI app in **main.py** that uses these CRUD operations:

```python
# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .crud import create_item, get_item, get_items, update_item, delete_item
from .models import Item

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/")
def create_item_route(item: Item, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db=db, skip=skip, limit=limit)

@app.put("/items/{item_id}")
def update_item_route(item_id: int, new_item: Item, db: Session = Depends(get_db)):
    item = update_item(db=db, item_id=item_id, new_item=new_item)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    item = delete_item(db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

In this example:

**/items/** POST endpoint creates a new item.
**/items/{item_id}** GET endpoint retrieves a specific item.
**/items/** GET endpoint retrieves a list of items with optional pagination (skip and limit).
**/items/{item_id}** PUT endpoint updates an item.
**/items/{item_id}** DELETE endpoint deletes an item.

You can run this FastAPI app with **uvicorn main:app --reload**. Use a tool like POSTMAN or CURL to interact with the CRUD endpoints. Adjust the code based on your specific requirements and database setup.
