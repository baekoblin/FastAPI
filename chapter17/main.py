# from fastapi import FastAPI, Depends, HTTPException, Path

# app = FastAPI()

# # 의존성 함수
# def get_current_user(token: str = Path(...)):
#     if token != "supersecrettoken":
#         raise HTTPException(status_code=400, detail="Invalid Token")
#     return {"username": "admin"}

# # API 엔드포인트
# @app.get("/users/me/{token}")
# async def read_current_user(current_user: dict = Depends(get_current_user)):
#     return current_user



# from fastapi import FastAPI, Depends, Query

# app = FastAPI()

# def get_user(username: str = Query(...)):
#     return {"username": username}

# @app.get("/users/")
# async def read_user(user: dict = Depends(get_user)):
#     return user


# # ---------------
# from fastapi import FastAPI, Depends
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     username: str
#     password: str

# def create_user(user: User):
#     return {"username": user.username, "created": "yes"}

# @app.post("/users/")
# async def create_user_route(new_user: dict = Depends(create_user)):
#     return new_user

# # -----------

# from fastapi import FastAPI, Depends, Header

# app = FastAPI()

# def get_token(token: str = Header(...)):
#     return {"token": token}

# @app.get("/token/")
# async def read_token(token_info: dict = Depends(get_token)):
#     return token_info



# ---------------

from fastapi import FastAPI, Depends

app = FastAPI()

def dependency_a():
    return "A"

def dependency_b():
    return "B"

def get_dependency(use_a: bool = True):
    if use_a:
        return dependency_a()
    else:
        return dependency_b()

@app.get("/choose/")
async def get_dependency_route(value: str = Depends(get_dependency)):
    return {"dependency_used": value}


