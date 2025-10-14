from fastapi import APIRouter, HTTPException, status, Path
from typing import Dict, List
from .cinehub_part3_models import MovieCreate, MovieUpdate, MovieOut

movies_router = APIRouter(prefix="/movies", tags=["Movies"], responses={404: {"description": "Not found"}})

# In-memory storage
_db: Dict[int, MovieOut] = {}
_next_id: int = 1

def _new_id() -> int:
    global _next_id
    nid = _next_id
    _next_id += 1
    return nid

@movies_router.post("/", response_model=MovieOut, status_code=status.HTTP_201_CREATED, summary="Create a movie")
def create_movie(payload: MovieCreate) -> MovieOut:
    mid = _new_id()
    movie = MovieOut(id=mid, archived=False, **payload.model_dump())
    _db[mid] = movie
    return movie

@movies_router.put("/{id}", response_model=MovieOut, summary="Update a movie by ID (partial fields allowed)")
def update_movie(
    id: int = Path(..., ge=0, description="Movie ID (>=0)"),
    payload: MovieUpdate = None
) -> MovieOut:
    if id < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID")
    if id not in _db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    existing = _db[id]
    data = existing.model_dump()
    for k, v in (payload.model_dump(exclude_unset=True)).items():
        data[k] = v
    updated = MovieOut(**data)
    _db[id] = updated
    return updated

@movies_router.get("/", response_model=List[MovieOut], summary="List all active (non-archived) movies")
def list_movies() -> List[MovieOut]:
    return [m for m in _db.values() if not m.archived]

@movies_router.get("/{id}", response_model=MovieOut, summary="Get movie by ID with error handling")
def get_movie(id: int = Path(..., description="Movie ID")) -> MovieOut:
    if id < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID")
    movie = _db.get(id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    if movie.archived:
        raise HTTPException(status_code=status.HTTP_410_GONE, detail="Movie archived")
    return movie

@movies_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Archive (soft-delete) a movie")
def delete_movie(id: int = Path(..., description="Movie ID")) -> None:
    if id < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID")
    movie = _db.get(id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    if movie.archived:
        raise HTTPException(status_code=status.HTTP_410_GONE, detail="Movie already archived")
    _db[id] = MovieOut(**{**movie.model_dump(), "archived": True})
    return
