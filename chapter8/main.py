from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/items")
async def read_time(request: Request):
    data = await request.json()
    return data
