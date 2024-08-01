from fastapi import FastAPI, Depends, Request, Header, HTTPException
import httpx
import asyncio

app = FastAPI()


### 의존성 오버라이딩
def dependency():
    return {"key": "original"}

@app.get("/")
def main(dep=Depends(dependency)):
    return dep

def override_dependency():
    return {"key": "overridden"}

app.dependency_overrides[dependency] = override_dependency


### 클래스 기반 의존성
class DatabaseConnection:
    def __init__(self, db_url: str):
        self.db_url = db_url

class Repo:
    def __init__(self, conn: DatabaseConnection = Depends()):
        self.conn = conn

@app.get("/repo_items/")
def read_items(repo: Repo = Depends()):
    return {"db_url": repo.conn.db_url}


### 사용자 정의 종속성을 반환하는 복잡한 의존성
def get_query():
    return {"q": "fastapi"}

def get_db():
    return {"db": "test_db"}

def complex_dependency(query=Depends(get_query), db=Depends(get_db)):
    return {"query": query, "db": db}

@app.get("/complex")
def read_complex_data(data=Depends(complex_dependency)):
    return data


### 스코프와 생명 주기
class ScopedConnection:
    def __init__(self, request: Request):
        self.request = request

@app.get("/scoped_items/")
async def read_scoped_items(conn: ScopedConnection = Depends(ScopedConnection)):
    return {"status": "new connection for each request"}


### 의존성 캐시
def common_parameters(q: str = None, page: int = 1, limit: int = 10):
    return {"q": q, "page": page, "limit": limit}

@app.get("/cached_items/")
def read_cached_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/cached_users/")
def read_cached_users(commons: dict = Depends(common_parameters)):
    return commons


### 의존성의 비동기 지원
async def get_remote_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
        return response.json()

@app.get("/external/")
async def external_data(data: dict = Depends(get_remote_data)):
    return data


### 의존성 주입을 사용한 테스트 가능한 코드
def secret_key_header(x_key: str = Header(...)):
    if x_key != "fake_secret_key":
        raise HTTPException(status_code=400, detail="Invalid X-Key header")
    return x_key

@app.get("/protected/")
def read_protected_data(secret_key: str = Depends(secret_key_header)):
    return {"message": "Secret data"}

app.dependency_overrides[secret_key_header] = lambda: "fake_secret_key"
