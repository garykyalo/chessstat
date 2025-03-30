from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from . services import ProcessScores, gamereviews

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


@router.api_route("/reviews", methods=["GET", "POST"])
async def Scores(request: Request):
    username = (await request.form()).get("username")
    results = gamereviews(username)  
    return templates.TemplateResponse(
        "review.html",
        {"request": request, "results": results, "user": username}
        )
    #return results 

   

@router.api_route("/analysis", methods=["GET", "POST"])
def Analysis():
    from .chessengine import  analysegame
    results =  analysegame()
    return results