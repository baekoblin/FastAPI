from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, update, delete

# 데이터베이스와 테이블 생성
engine = create_engine('sqlite:///example.db', echo=True)
metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer))
metadata.create_all(engine)

# 데이터 조회
try:
    with engine.connect() as conn:
        result = conn.execute(select(users))
        rows = result.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")

# 데이터 삽입
with engine.connect() as conn:
    conn.execute(insert(users).values(name='Alice', age=30))
    conn.execute(insert(users), [{'name': 'Bob', 'age': 20}, {'name': 'Carol', 'age': 25}])
    conn.commit()  # 변경 사항 커밋

# 데이터 조회
try:
    with engine.connect() as conn:
        result = conn.execute(select(users))
        rows = result.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")

# 데이터 업데이트
with engine.connect() as conn:
    conn.execute(update(users).where(users.c.name == 'Alice').values(age=31))
    conn.commit()  # 변경 사항 커밋

# 데이터 조회
try:
    with engine.connect() as conn:
        result = conn.execute(select(users))
        rows = result.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")

# 데이터 삭제
with engine.connect() as conn:
    conn.execute(delete(users).where(users.c.name == 'Bob'))
    conn.commit()  # 변경 사항 커밋

# 데이터 조회
try:
    with engine.connect() as conn:
        result = conn.execute(select(users))
        rows = result.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")


from sqlalchemy import func

# 연령 그룹별 평균 나이 계산 및 이름으로 정렬
try:
    with engine.connect() as conn:
        # 쿼리 수정: 컬럼을 명시적으로 select 함수에 전달
        age_group_query = select(
            users.c.name,
            func.avg(users.c.age).label('average_age')
        ).group_by(users.c.name).order_by(users.c.name)

        result = conn.execute(age_group_query)
        for row in result:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")
