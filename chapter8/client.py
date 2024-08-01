import requests
import json

url = 'http://localhost:8000/items'  # FastAPI 서버 URL 및 엔드포인트
data = {'key': 'value'}  # 전송할 JSON 데이터

response = requests.post(url, json=data)  # POST 요청
print("Status Code:", response.status_code)
print("JSON Response:", response.json())