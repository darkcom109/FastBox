# Import instance from FastAPI, Form lets us accept form data (what user pastes)
from fastapi import FastAPI, Form, Request

# Tells FastAPI to return HTML not JSON
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Tells FastAPI where templates live
templates = Jinja2Templates(directory="templates")

app = FastAPI(title="FastBox", version="1.0") #  Instantiate object
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route for homepage, parameter tells FastAPI to return the string as raw HTML
# Includes a form where users submit the data to /preview
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    

# This is the endpoint to receive form submission
@app.post("/preview", response_class=HTMLResponse)
def preview(request: Request, code: str = Form(...)):
    return templates.TemplateResponse("preview.html", {"request": request, "code": code})