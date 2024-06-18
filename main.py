from fastapi import FastAPI, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Union
import io
from PIL import Image
from modules.model import model_pipeline

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.post("/ask")
async def ask(text: str = Form(...), image: UploadFile = Form(...)):
    content = await image.read()

    image = Image.open(io.BytesIO(content))
    result = model_pipeline(text, image)
    return {"answer": result}
