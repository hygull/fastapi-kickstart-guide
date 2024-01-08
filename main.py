from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from enum import Enum
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request


app = FastAPI()


@app.get('/')
def hello_programmers():
    return {
        "status": 200,
        "message": "Hello Programmers"
    }


@app.get('/users')
def hello_programmers(
        first_name: str,
        last_name: str
    ):
    return {
        "status": 200,
        "message": "Hello Programmers",
        "user": {
            "first_name": first_name,
            "last_name": last_name
        }
    }


@app.get('/default-users')
def hello_programmers(
        first_name: str = 'Default first name',
        last_name: str = "Default last name",
        age: int = 0,
        city: str = 'Bangalore'
    ):
    return {
        "status": 200,
        "message": "Hello Programmers",
        "user": {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "city": city
        }
    }


@app.get('/validate')
def validate_integer_numbers(
        number: str
    ):
    try:
        number = float(number) if '.' in number else int(number)
        return {
            "message": f"{number} is a valid number of {type(number)}"
        } 
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{number} is an invalid number of {type(number)} -> {error}")


class User(BaseModel):
    first_name: str
    last_name: str
    full_name: str = ''
    username: str
    age: int
    city: str


@app.post("/users/create/")
def create_user(
        user: User
    ):
    user.full_name = f"{user.first_name} {user.last_name}"
    return user


class State(BaseModel):
    name: str
    blocks: int
    pincode: int

class City(BaseModel):
    name: str
    state: State
    population: int
    pincode: int

@app.post("/cities/create")
def create_city(
        city: City
    ):
    return city


class Fruit(BaseModel):
    name: str 
    colour: str

class Tree(BaseModel):
    name: str
    branches: int
    leaves: int
    fruits: List[Fruit]

@app.post("/trees/create")
def create_tree(
        tree: Tree
    ):
    return tree


class FruitName(str, Enum):
    default = 'fruit'
    favourite = 'favourite fruit'
    healthy = 'healthy fruit'


@app.post('/fruits/create')
def create_fruit(
        name: str, 
        nickname: FruitName
    ):
    return {
        "fruit": {
            "name": name,
            "nickname": nickname
        }
    }

class CustomFastAPIHttpException(HTTPException):
    def __init__(self, status_code: int, detail: str, custom_message: str):
        super().__init__(status_code=status_code, detail=detail)
        self.custom_message = custom_message

    # def as_response(self):
    #     return JSONResponse(
    #         status_code=self.status_code,
    #         content= {
    #             "detail": self.detail,
    #             "custom_message": self.custom_message
    #         }
    #     )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exception: RequestValidationError
):
    return JSONResponse(
        status_code=exception.status_code,
        content= {
            "detail": exception.errors()
        }
    )


@app.get("/plans/")
def get_plans(
        count: int
    ):
    try:
        assert count != 0, "Plans count should be > 0"
        return {
            "plans": [
                { 
                    "name": f"Plan {plan_no}", 
                    "created_at": datetime.now(),
                    "updated_at": datetime.now()
                }
                for plan_no in range(1, count + 1)
            ]
        }
    except Exception as error:
        raise CustomFastAPIHttpException(
            status_code=400,
            detail=f'There is some issue while processing the request -> {error}',
            custom_message='Please check, this might be due to wrong input or code BUG'
        )