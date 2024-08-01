from fastapi import FastAPI, Request
from loguru import logger

app = FastAPI()

logger.add("file_{time}.log")

@app.middleware("http")
async def log_requests(request:Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

@app.get("/")
async def read_root():
    return {"hello":"logger"}