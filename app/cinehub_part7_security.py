from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException, Header, Query, status

VALID_TOKEN = "letmein"

def verify_token(
    x_token: Optional[str] = Header(default=None, alias="X-Token"),
    token_q: Optional[str] = Query(default=None, alias="token"),
) -> str:
    token = x_token or token_q
    if token != VALID_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return token

TokenDep = Annotated[str, Depends(verify_token)]

secure_router = APIRouter(prefix="/secure", tags=["Security"], dependencies=[Depends(verify_token)])

@secure_router.get("/ping", summary="Protected ping via router-level dependency")
def secure_ping():
    return {"result": "pong-secure"}

def secure_data(token: TokenDep):
    return {"message": "Secure data access granted", "token_used": token}
