from fastapi import APIRouter, HTTPException
from utils.token_manager import login

user_router = APIRouter()

@user_router.post("/login",tags=["authentication"])
async def auth(username: str, password: str):
    api_key = login(username, password)
    if api_key:
        return {"api_key": api_key}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")