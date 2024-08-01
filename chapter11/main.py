from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

async def get_remote_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json
    
@app.get("/data")
async def read_data():
    external_data = await get_remote_data("exameple")
    return external_data