from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import subprocess
import sys
import subprocess
import sys
from pathlib import Path

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates
templates = Jinja2Templates(directory="templates")

gesture_process = None


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.get("/instructions.html")
async def instructions(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="instructions.html",
        context={"request": request}
    )


@app.post("/start")
async def start():
    global gesture_process

    gesture_path = Path(__file__).parent / "gesture.py"
    print("Gesture path:", gesture_path)

    gesture_process = subprocess.Popen(
        [sys.executable, str(gesture_path)]
    )

    print("Started:", gesture_process.pid)
    return {"message": "Started"}


@app.post("/stop")
async def stop():
    global gesture_process

    if gesture_process:
        gesture_process.terminate()
        gesture_process = None

    return {"message": "Stopped"}
