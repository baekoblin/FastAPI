from starlette.applications import Starlette
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import time

class SimpleRateLimiter(BaseHTTPMiddleware):
    def __init__(self, app, limit=100):
        super().__init__(app)
        self.limit = limit
        self.requests = 0
        self.start_time = time.time()

    async def dispatch(self, request: Request, call_next):
        if time.time() - self.start_time > 60:
            self.requests = 0
            self.start_time = time.time()

        if self.requests < self.limit:
            self.requests += 1
            response = await call_next(request)
            return response
        else:
            return PlainTextResponse("Too Many Requests", status_code=429)

async def homepage(request):
    return PlainTextResponse('Hello, world!')

app = Starlette(debug=True, routes=[
    Route('/', homepage),
])

app.add_middleware(SimpleRateLimiter, limit=5)  # 매분 최대 5개 요청 허용

