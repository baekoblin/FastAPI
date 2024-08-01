from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/items")
async def items(x_token: str = Header(...)):  # Use x_token or a suitable name that matches the expected header key
    return {"test": "response " + x_token}