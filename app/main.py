from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .cinehub_part2_params import params_router
from .cinehub_part3_models import MovieCreate, MovieUpdate, MovieOut  # expose in docs
from .cinehub_part4_routers import health_router, info_router
from .cinehub_part5_retrieval import movies_router
from .cinehub_part6_templates import html_router
from .cinehub_part7_security import secure_router, secure_data, verify_token

app = FastAPI(title="CineHub FastAPI", version="1.0.0", description="A modular FastAPI demo app for assignments")

@app.get("/hello", summary="Hello route", description="Returns a plain greeting to verify the app runs.")
def hello():
    return {"message": "Hello, world!"}

static_dir = Path(__file__).resolve().parents[1] / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

app.include_router(params_router)
app.include_router(health_router)
app.include_router(info_router)
app.include_router(movies_router)
app.include_router(html_router)
app.include_router(secure_router)

@app.get("/secure-data", tags=["Security"], summary="Protected endpoint via function-level dependency")
def read_secure_data(token: str = Depends(verify_token)):
    return secure_data(token)
