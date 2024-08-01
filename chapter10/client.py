import requests

# API 엔드포인트 URL
url = "http://127.0.0.1:8000/user/"

# 보낼 데이터
data = {
    "name": "홍길동",
    "age": 25
}

# POST 요청
response = requests.post(url, json=data)

# 응답 데이터 출력
print("Status Code:", response.status_code)
print("Response Data:", response.json())
