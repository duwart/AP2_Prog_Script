from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
# In templates will be the html files
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def name(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.post("/")
async def calculate(data: dict):
    result = data.get("number")
    
    if result is not None:
        result = result + 2
    
    return {"result": result}
