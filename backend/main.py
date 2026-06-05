from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Novel2Script API")


class NovelRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Novel2Script API is running"}


@app.post("/generate")
def generate_script(request: NovelRequest):
    return {
        "title": "Generated Script",
        "input_length": len(request.text),
        "status": "success"
    }
