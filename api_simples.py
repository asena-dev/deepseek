# GET -> Buscar dados
# POST -> Enserir dados
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message":"Olá, FastAPI!"}