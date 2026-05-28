from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

client = APIRouter(prefix='/app')

templates = Jinja2Templates(directory="templates")

@client.get("/", response_class=HTMLResponse)
async def main_page(request: Request, user_id: int):
    return templates.TemplateResponse(
        "chat.html", 
        {"request": request, "user_id": user_id}
    )