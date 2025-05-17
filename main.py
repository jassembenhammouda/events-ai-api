# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Lire la variable d'environnement pour le token Hugging Face
HUGGINGFACE_API_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate-image")
def generate_image(req: PromptRequest):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": req.prompt})
    return {"status_code": response.status_code, "image": response.content}
