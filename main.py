from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "반가워요 여러분"}


@app.get("test")
async def test():
    return {"message": "테스트 해보기 예제"}
