from fastapi import APIRouter

health_router = APIRouter(prefix="/health", tags=["Health"])

@health_router.get("/live", summary="Liveness probe")
def live():
    return {"status": "ok"}

@health_router.get("/ready", summary="Readiness probe")
def ready():
    return {"status": "ready"}

info_router = APIRouter(prefix="/info", tags=["Info"])

@info_router.get("/", summary="Service info")
def info():
    return {"service": "cinehub-fastapi", "version": "1.0.0"}
