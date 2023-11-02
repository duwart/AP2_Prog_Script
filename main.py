from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
# In templates will be the html files
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def name(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate/")
async def calculate(request: Request, data: dict):
    number = data.get("number")
    if number is not None:
        result = number + 2
        return {"result": result}
    else:
        return {"result": "Erro: número não especificado"}
