from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from enum import Enum


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


class PlatformType(str, Enum):
    search_engine = 'Search Engine'
    social_media = 'Social Media'


class PlatformInfo(BaseModel):
    name: str 
    type: PlatformType
    nickname: str


class Platform(Enum):
    instagram = PlatformInfo(
        name="Instagram", 
        type=PlatformType.social_media, 
        nickname=f'Instagram {PlatformType.social_media.value}'
    )
    facebook = PlatformInfo(
        name="Facebook", 
        type=PlatformType.social_media, 
        nickname=f'Facebook {PlatformType.social_media.value}'
    )
    google = PlatformInfo(
        name="Google", 
        type=PlatformType.search_engine, 
        nickname=f'Google {PlatformType.search_engine.value}'
    )


class PlatformRequest(BaseModel):
    platform: str


@app.post("/platforms/create")
def create_platform(
        platform_request: PlatformRequest
    ):
    try:
        platform = Platform[platform_request.platform].value.dict()
    except KeyError as error:
        # Order is status_code, detail -> if you do not specify kwarg names then using 
        #   `raise HTTPException(f'Invalid key {platform_request.platform}', status_code=400)`
        # will throw
        #   `TypeError: HTTPException.__init__() got multiple values for argument 'status_code'`
        raise HTTPException(
            detail=f'Invalid key {platform_request.platform}', 
            status_code=400
        ) 

    return {
        "platform": platform
    }