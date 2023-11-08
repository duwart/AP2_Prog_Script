from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Dict

# Aqui é criada uma instância de FastApi
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# A função abaixo é responsável por tratar as requisições que vão para a rota '/'
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.post(
        "/result/", 
        status_code=status.HTTP_201_CREATED, 
        response_model=Dict[str, float],
        summary="Operação de soma",
        description="Soma o número definido pelo usuário com o valor 2",
    )
async def calculate(data: Dict[str, float]):
    result = data.get("number")
    
    if result is not None:
        result = result + 2
    
    return {"result": result}
