## Is there any JOIN examples as well using the Post model (Post here I mean the posts created by user -> id, title, caption, etc.)!


Certainly! Let's extend the example to include a Post model and demonstrate some JOIN examples:

**Define the Post Model:**

Update the models.py file to include the Post model:

```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")
```

**Update the User Model:**

Add a relationship to the User model to link it with posts:

```python
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    posts = relationship("Post", back_populates="author")
```

**Apply Migrations:**

Generate a new migration and apply it to update the database schema to include the Post model.

**Querying with JOINs:**
Here are some examples of querying with JOINs in FastAPI:

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(models.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, db: Session = Depends(models.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts

@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(models.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
```

These endpoints demonstrate how to query users along with their associated posts and retrieve individual posts. You can further expand these endpoints to suit your application's needs, such as filtering, pagination, or additional data fetching.

With these examples, you now have a basic understanding of how to use JOINs in FastAPI applications with SQLAlchemy models to retrieve related data from multiple tables.
