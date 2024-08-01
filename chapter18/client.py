import httpx
import asyncio

async def main():
    base_url = "http://127.0.0.1:8000"  # FastAPI 서버의 주소

    # '/' 엔드포인트 호출
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/")
        print("Main Response:", response.json())

    # '/repo_items/' 엔드포인트 호출
        response = await client.get(f"{base_url}/repo_items/")
        print("Repo Items Response:", response.json())

    # '/complex' 엔드포인트 호출
        response = await client.get(f"{base_url}/complex")
        print("Complex Data Response:", response.json())

    # '/scoped_items/' 엔드포인트 호출
        response = await client.get(f"{base_url}/scoped_items/")
        print("Scoped Items Response:", response.json())

    # '/cached_items/' 엔드포인트 호출
        response = await client.get(f"{base_url}/cached_items/")
        print("Cached Items Response:", response.json())

    # '/cached_users/' 엔드포인트 호출
        response = await client.get(f"{base_url}/cached_users/")
        print("Cached Users Response:", response.json())


    # '/protected/' 엔드포인트 호출 (올바른 헤더 제공)
        headers = {'X-Key': 'fake_secret_key'}
        response = await client.get(f"{base_url}/protected/", headers=headers)
        print("Protected Data Response:", response.json())

# 비동기 main 함수 실행
asyncio.run(main())
