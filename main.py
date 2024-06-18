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
    """
    This function handles the GET request to the root ('/') endpoint.
    It serves the static HTML file 'index.html' from the 'static' directory.

    Parameters:
    - None

    Returns:
    - FileResponse: A response object containing the static HTML file 'index.html'.

    Raises:
    - None
    """
    return FileResponse("static/index.html")


@app.post("/ask")
async def ask(text: str = Form(...), image: UploadFile = Form(...)):
    """
    This function handles the POST request to the '/ask' endpoint.
    It receives a text question and an image, processes them, and returns the answer.

    Parameters:
    - text (str): The text question. It is optional and can be provided as a form parameter.
    - image (UploadFile): The image file. It is optional and can be provided as a form parameter.

    Returns:
    - dict: A dictionary containing the answer to the question.

    Raises:
    - Exception: If any error occurs during the processing of the question or image.
    """
    content = await image.read()  # Read the content of the uploaded image

    image = Image.open(io.BytesIO(content))  # Open the image using PIL

    # Process the question and image using the model pipeline
    result = model_pipeline(text, image)

    return {"answer": result}  # Return the answer as a JSON response
