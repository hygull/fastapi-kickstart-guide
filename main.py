from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def hello_programmers():
	return {
		"status": 200,
		"message": "Hello Programmers"
	}