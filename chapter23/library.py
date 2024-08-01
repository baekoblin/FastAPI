from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.responses import PlainTextResponse

app = FastAPI()

# 리미터 객체 생성, 클라이언트 IP 주소를 기준으로 속도 제한 설정
limiter = Limiter(key_func=get_remote_address)
# SlowAPIMiddleware를 애플리케이션에 추가하고, limiter 인스턴스를 사용하도록 설정
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
@limiter.limit("5/minute")  # 분당 최대 5회 요청 제한
async def home(request: Request):
    return PlainTextResponse("Welcome to the rate limited API!")

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return PlainTextResponse("Too Many Requests", status_code=429)
