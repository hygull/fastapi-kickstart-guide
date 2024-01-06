# fastapi-kickstart-guide
A repository which contains beautiful notes and steps which can help beginners of FastAPI to kickstart with the FastAPI very faster. It contains bunch of beautiful examples, learning notes, references etc. Images have been attached too. The README.md will help any newbies to FastAPI learn the things faster and better.

## List of contents

1. [Cloning newly created Github project and dependencies installation inside virtualenv](./resources/docs/01_virtualenv_and_dependencies_installations.md)
2. [Create main application file, write starter endpoint and run server](./resources/docs/02_create_main_application_file_and_runserver.md)

---

**Create `main.py` with below code snippet**

```python
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def hello_programmers():
    return {
        "status": 200,
        "message": "Hello Programmers"
    }
```
---

> **Run the app server**
>
> By default it runs on port `8000` (Here I am running on a custom port `9000`)

`uvicorn main:app --reload --port 9000`

![Run server and test the API](./resources/images/01_postman_hello_world_my_first_fast_api_endpoint_from_scratch.png)

---

**Query Parameters**

```python
from fastapi import FastAPI


app = FastAPI()

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
```

-> Query Parameters

![Query Parameters Example](./resources/images/02_postman_query_parameters_example.png)

-> Required Query Parameters (Automatic validations)
![Required Query Parameters Example](./resources/images/03_required_query_parameters.png)

---

**Query Parameters with default values**

```python
from fastapi import FastAPI


app = FastAPI()

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
```

-> Query parameters with default values

![Query parameters with default values](./resources/images/04_query_parameters_with_default_values.png)

---

**Handing Exceptions**

```python
from fastapi import FastAPI, HTTPException


app = FastAPI()

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
```

-> Handing Exceptions - valid response 

![Handing Exceptions v1](./resources/images/05_handing_exceptions_1.png)
---
Handing Exceptions - Invalid response 
![Handing Exceptions v2](./resources/images/05_handing_exceptions_2.png)

---

**Pydantic Model for Input validation**

```python
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    full_name: str = '' # Skipping this entry will raise `ValueError: "User" object has no field "full_name" inside endpoint while setting -> user.full_name` 
    username: str
    age: int
    city: str

@app.post("/users/create/")
def create_user(
        user: User
    ):
    user.full_name = f"{user.first_name} {user.last_name}"
    return user
```
-> 2 fields are missing in the POST body

![Pydanctic Model for input validation v1](./resources/images/06_pydantic_model_input_validation_1.png)

-> 1 field is missing in the POST body

![Pydanctic Model for input validation v2](./resources/images/07_pydantic_model_input_validation_2.png)

-> All the fields are being passed in the POST body (full_name field is optional with default value `''` i.e. blank string)
![Pydanctic Model for input validation v3](./resources/images/08_pydantic_model_input_validation_3.png)

---

**Nested POST Body**

> Note: Here I have considered `blocks` as `no_of_blocks` and not the actual block instances. 

```python
from fastapi import FastAPI
from pydantic import BaseModel


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
```

-> Nested POST body: State is nested inside City

![Nested POST body](./resources/images/09_nested_post_body_example.png)

---

**POST body with List of objects**

```python
from fastapi import FastAPI
from typing import List


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
```

-> POST body with list of objects (List of Fruits objects inside the Tree object)

![POST body with list of objects](./resources/images/10_post_body_with_list_of_objects.png)

---

**Using Enum for input validation**

```python
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
```

-> If wrong value is passed for Enum data type

![If wrong value is passed for Enum data type](./resources/images/11_enum_input_validation_error_example.png)


-> If correct values are passed for Enum data type

![If correct values are passed for Enum data type](./resources/images/12_enum_input_validation_success_example.png)

---

### Error Patterns

- A Database error occurred (If VPN is not connected OR internet is too slow).
- Detail not found (If wrong FastAPI app is running and we are hitting the API).
- Internal Server Error (Not handling an exception inside the endpoint function throws this).

### Notes 

- Not returning anything from endpoint returns null response.

### API/FastAPI specific keywords

- Path 
- Route
- Route definition
- Endpoint
- HTTP method/verb
- Path parameters
- Query parameters

### References

- [How to run FastAPI app on a custom port](https://www.slingacademy.com/article/how-to-run-fastapi-on-a-custom-port/)
- [How to extract Query parameters in FastAPI](https://www.slingacademy.com/article/how-to-extract-query-parameters-in-fastapi/)
