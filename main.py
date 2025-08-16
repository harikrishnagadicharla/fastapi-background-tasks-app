from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time
import os

app = FastAPI()

# Static & Template setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Background Task - Email
def send_email_background(email: str, message: str):
    time.sleep(5)
    with open("sent_emails.log", "a") as f:
        f.write(f"Email sent to {email} with message: {message}\n")

# Background Task - File
def process_file_background(file_path: str):
    time.sleep(10)
    with open("processed_files.log", "a") as f:
        f.write(f"Processed file: {file_path}\n")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send-email/")
async def send_email(background_tasks: BackgroundTasks, email: str = Form(...), message: str = Form(...)):
    background_tasks.add_task(send_email_background, email, message)
    return {"status": "Email will be sent in the background"}

@app.post("/upload-file/")
async def upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    background_tasks.add_task(process_file_background, file_location)
    return {"status": "File uploaded successfully, processing in background"}
