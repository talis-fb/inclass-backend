from fastapi import FastAPI

BANCO_DE_DADOS = [
    {"id": 1, "name": "João"},
    {"id": 2, "name": "Maria"},
    {"id": 3, "name": "Pedro"},
]

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):
    for user in BANCO_DE_DADOS:
        if user["id"] == id:
            return user

@app.post("/users/{name}")
def create_user(name: str):
    new_id = len(BANCO_DE_DADOS) + 1
    new_user = {
        "id": new_id,
        "name": name
    }

    BANCO_DE_DADOS.append(new_user)

    return {
        "id": new_id
    }

@app.put("/users/{id}")
def update_user(id: int, item: str):
    for user in BANCO_DE_DADOS:
        if user["id"] == id:
            user["name"] = item
            return user
