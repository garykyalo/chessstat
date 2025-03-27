from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from . services import ProcessScores

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.api_route("/", methods=["GET", "POST"])
async def home(request: Request):
    return templates.TemplateResponse(
        "chess.html",
        {"request": request}
    )

@router.api_route("/scores", methods=["GET", "POST"])
def Scores():
    results1 = ProcessScores()
    return results1