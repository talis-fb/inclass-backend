from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "Hello": name
    }
