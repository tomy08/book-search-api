from fastapi import APIRouter, HTTPException,JsonResponse
from utils.token_manager import login

user_router = APIRouter()

@user_router.post("/login")
async def login(username: str, password: str):
    api_key = login(username, password)
    if api_key:
        return JsonResponse({"api_key": api_key})
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")