from fastapi import FastAPI, Depends

app = FastAPI()

# 데이터베이스 연결을 시뮬레이션하는 클래스
class DBConnection:
    def __init__(self):
        self.conn = "Database Connection"

    async def __call__(self):
        # 실제 환경에서는 여기에서 데이터베이스 연결 로직을 실행할 것입니다.
        return self.conn

# 의존성 인스턴스를 생성합니다.
db_connection = DBConnection()

# 의존성 함수
async def get_db_connection():
    return await db_connection()

# FastAPI 경로 작업
@app.get("/items/")
async def read_items(conn: str = Depends(get_db_connection, use_cache=True)):
    # 첫 번째 호출에서 의존성을 계산하고, 같은 요청 동안의 후속 호출에서 캐시된 값을 사용합니다.
    return {"database_connection": conn}

@app.get("/more-data/")
async def read_more_data(conn: str = Depends(get_db_connection, use_cache=True)):
    # 같은 요청에서 이전에 캐시된 데이터베이스 연결을 재사용합니다.
    return {"database_connection": conn}
