# FastAPI script
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/button")
async def color_change(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/")
@app.get("/HomePage")
async def Main(request: Request):
    return templates.TemplateResponse("Home.html", {"request": request})


