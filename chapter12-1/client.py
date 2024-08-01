import requests

# FastAPI 서버의 URL
base_url = "http://127.0.0.1:8000"

# 루트 경로 테스트
response = requests.get(f"{base_url}/")
print(f"Response from '/': {response.json()}")

# 유효한 토큰을 사용하여 아이템 조회
valid_token = "secret"
response = requests.get(f"{base_url}/items/1", params={"token": valid_token})
print(f"Response from '/items/1' with valid token: {response.json()}")

# 유효하지 않은 토큰으로 아이템 조회
invalid_token = "invalid"
response = requests.get(f"{base_url}/items/1", params={"token": invalid_token})
print(f"Response from '/items/1' with invalid token: {response.status_code}")

# 아이템 추가
response = requests.post(f"{base_url}/items/", json={"name": "new_item"})
print(f"Response from POST '/items/': {response.json()}")
