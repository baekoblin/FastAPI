from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    name: str
    age: int
    is_adult: bool

@app.post("/user", response_model=UserResponse)
def create_user(user: UserInput):
    # 입력 받은 데이터를 처리합니다.
    is_adult = user.age >= 18
    # 응답 모델을 사용하여 응답 데이터를 구성합니다.
    response_data = UserResponse(
        name=user.name,
        age=user.age,
        is_adult=is_adult
    )
    return response_data
