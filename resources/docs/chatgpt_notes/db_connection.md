## How to connect to DB in FastAPI?

FastAPI itself doesn't dictate how you should connect to a database; it provides the flexibility for you to choose the database and the method of connection that fits your needs. The common practice is to use an ORM (Object-Relational Mapping) library with FastAPI, and SQLAlchemy is a popular choice.

Here is a step-by-step guide on how to connect to a database using SQLAlchemy in FastAPI:

Install Required Packages:
Install FastAPI and the database library of your choice (in this case, SQLAlchemy). For example, to install both FastAPI and SQLAlchemy, you can use:

bash

```bash
pip install fastapi[all] sqlalchemy
```

The [all] extra installs additional dependencies, including uvicorn for ASGI support.

Create a Database Session:
You need a database session to interact with the database. Use SQLAlchemy to create a session. Here's an example:


```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

The DATABASE_URL is a URL that specifies the database engine and connection details.

Use Dependency Injection for Dependency Management:
FastAPI allows you to use dependency injection to manage dependencies like the database session. You can create a dependency that provides a database session to your API routes:

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

You can then use Depends(get_db) in your route functions to obtain a database session.

Use the Database Session in Your Routes:
Now, you can use the database session in your FastAPI routes. For example:

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, database

app = FastAPI()

@app.post("/items/")
def create_item(item: Item, db: Session = Depends(database.get_db)):
    return crud.create_item(db=db, item=item)
```

In this example, the create_item route depends on the database session (db: Session = Depends(database.get_db)). The crud.create_item function can then use this session to interact with the database.

Remember to replace the placeholders and adapt the code according to your specific database engine, model structure, and requirements.