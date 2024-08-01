from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
