from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from ai.llm import answer

app = FastAPI(title="Caleb GPT")

path = Path(__file__).parent / "static"


@app.get("/")
def index():
    return FileResponse(path / "index.html")


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(req: ChatRequest):
    response = answer(req.question)
    return {"content": response}
