from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
users_db = []

# Modelo de dados
class User(BaseModel):
    name: str
    age: int

@app.post("/create_user")
def create_user(user:User):
    users_db.append(user)
    if user.age < 18:
        return {"message": f"Olá {user.name}! Você é menor de idade, tenha um péssimo dia!"}
    return {"message": f"Olá {user.name}! Você tem {user.age} de idade, tenha um ótimo dia!"}

@app.get("/users", response_model=List[User])
def get_users():
    return users_db