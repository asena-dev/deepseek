import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

# Agora a chave de API é carregada corretamente do .env
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    api_key=os.getenv("GROQ_API_KEY")  # <-- Aqui está o ajuste!
)
app = FastAPI()

messages = []

class MessageResquest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_ai(request: MessageResquest):
    messages.append(("human", request.message))
    response = llm.invoke(messages).content
    messages.append(("ai", response))
    return {"response": response}

@app.get("/messages")
async def get_messages():
    return {"messages": [{"type": msg[0], "content": msg[1]} for msg in messages]}