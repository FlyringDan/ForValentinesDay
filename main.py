from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static/pictures", StaticFiles(directory="static/pictures"), name="static")
templates = Jinja2Templates(directory="static/templates")

@app.get("/love", response_class=HTMLResponse)
async def love(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )