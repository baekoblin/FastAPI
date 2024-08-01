from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status
from enum import Enum
from typing import List

class Role(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"

class User(BaseModel):
    username: str
    roles: List[Role]

# 예제 사용자 데이터베이스
users_db = {
    "alice": User(username="alice", roles=[Role.admin, Role.user]),
    "bob": User(username="bob", roles=[Role.user]),
    "eve": User(username="eve", roles=[Role.guest])
}

def get_current_user(username: str) -> User:
    if username in users_db:
        return users_db[username]
    raise HTTPException(status_code=404, detail="User not found")

def role_checker(required_roles: List[Role]):
    def role_dependency(user: User = Depends(get_current_user)):
        if any(role in user.roles for role in required_roles):
            return user
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted"
        )
    return role_dependency

app = FastAPI()

@app.get("/data/{username}", dependencies=[Depends(role_checker([Role.admin, Role.user]))])
async def read_data(username: str):
    return {"username": username, "data": "Some secure data"}

@app.post("/admin/data", dependencies=[Depends(role_checker([Role.admin]))])
async def update_data(data: dict, user: User = Depends(get_current_user)):
    return {"user": user.username, "data_received": data}
