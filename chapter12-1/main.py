from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# 종속성 주입을 위한 함수
def verify_token(token: str):
    if token != "secret":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token

# 아이템 모델
class Item(BaseModel):
    name: str

# 루트 경로
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# 아이템 경로 (종속성 주입 사용)
@app.get("/items/{item_id}")
async def read_item(item_id: int, token: str = Depends(verify_token)):
    return {"item_id": item_id, "token": token}

# 아이템 추가 경로 (POST 요청)
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return {"name": item.name}
