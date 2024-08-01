import requests

# FastAPI 서버 주소
base_url = "http://127.0.0.1:8000"

# 올바른 API 키로 사용자 정보 요청
headers = {"API-Key": "secret"}
response = requests.get(f"{base_url}/users/me", headers=headers)
print("Response with valid API key:", response.json())

# 잘못된 API 키로 사용자 정보 요청
wrong_headers = {"API-Key": "invalid_key"}
response = requests.get(f"{base_url}/users/me", headers=wrong_headers)
print("Response with invalid API key:", response.status_code, response.text)
