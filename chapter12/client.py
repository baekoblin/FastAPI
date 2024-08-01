import requests

# FastAPI 서버의 URL
base_url = "http://127.0.0.1:8000"

# 루트 경로에 GET 요청
response = requests.get(f"{base_url}/")
print(f"Response from '/': {response.json()}")

# /items/1 경로에 GET 요청
item_id = 1
response = requests.get(f"{base_url}/items/{item_id}")
print(f"Response from '/items/{item_id}': {response.json()}")
