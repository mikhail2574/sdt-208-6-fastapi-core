from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .cinehub_part5_retrieval import _db

templates_dir = Path(__file__).resolve().parents[1] / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

html_router = APIRouter(prefix="/movies", tags=["Movies HTML"])

@html_router.get("/html", response_class=HTMLResponse, summary="Render movies list", name="movies_html")
def movies_html(request: Request):
    movies = list(_db.values())
    return templates.TemplateResponse("movies/list.html", {"request": request, "movies": movies})

@html_router.get("/{id:int}/html", response_class=HTMLResponse, summary="Render movie details", name="get_movie_html")
def get_movie_html(id: int, request: Request):
    movie = _db.get(id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return templates.TemplateResponse("movies/detail.html", {"request": request, "movie": movie})
