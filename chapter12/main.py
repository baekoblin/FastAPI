from fastapi import FastAPI, Request
import time
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print("Hello It's Me")
        response = await call_next(request)
        return response

app.add_middleware(CustomMiddleware)

# 미들웨어 정의
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    # 요청 처리
    response = await call_next(request)
    # 처리 시간 계산
    process_time = time.time() - start_time
    # 로그 출력
    print(f"Request: {request.method} {request.url} - Completed in {process_time} secs")
    return response

# 예시 경로
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
