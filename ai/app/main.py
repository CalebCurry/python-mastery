from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from ai.llm import answer

app = FastAPI(title="Caleb GPT")

path = Path(__file__).parent / "static"
lessons_path = Path(__file__).parent.parent / "lessons"


@app.get("/")
def index():
    return FileResponse(path / "index.html")


@app.get("/api/lessons")
def get_lessons():
    lesson_files = sorted(lessons_path.glob("lesson-*.md"))
    lessons = []
    for file in lesson_files:
        lesson_id = file.stem.replace("lesson-", "")
        with open(file, "r") as f:
            first_line = f.readline().strip()
            title = first_line.replace("#", "").strip() if first_line.startswith("#") else file.stem
        lessons.append({"id": lesson_id, "title": title, "filename": file.name})
    return {"lessons": lessons}


@app.get("/api/lessons/{lesson_id}")
def get_lesson(lesson_id: str):
    lesson_file = lessons_path / f"lesson-{lesson_id}.md"
    if not lesson_file.exists():
        raise HTTPException(status_code=404, detail="Lesson not found")
    with open(lesson_file, "r") as f:
        content = f.read()
    return {"content": content}


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(req: ChatRequest):
    response = answer(req.question)
    return {"content": response}
