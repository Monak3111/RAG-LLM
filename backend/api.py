from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rag import ask_ai


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get("/")
def home():
    return {
        "status":"RAG API running"
    }



@app.post("/chat")
def chat(data:dict):

    question=data["question"]

    answer=ask_ai(question)

    return {
        "answer":answer
    }