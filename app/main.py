from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Add CORS middleware (if accessing from different origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Serve static files (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

class Input(BaseModel):
    age: int
    sex: str

@app.put("/predict")
def predict_model(d: Input):
    if d.age < 16 or d.sex == 'F':
        return {'survived': 1}
    else:
        return {'survived': 0}

# Serve the main HTML file
@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    with open(os.path.join('static', 'index.html')) as f:
        return HTMLResponse(content=f.read())
