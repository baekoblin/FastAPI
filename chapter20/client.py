import requests

# API 서버의 URL
BASE_URL = "http://localhost:8000"

def get_token(username: str, password: str):
    url = f"{BASE_URL}/token"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=data)
    return response.json()  # 토큰 정보를 반환

def get_user_details(token: str):
    url = f"{BASE_URL}/users/me/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()  # 유저 정보를 반환

# 사용자의 username과 password
username = "johndoe"
password = "secret"

# 토큰 받아오기
token_response = get_token(username, password)
if "access_token" in token_response:
    token = token_response["access_token"]
    print("Token received:-", token)
    # 토큰을 사용하여 유저 정보 가져오기
    user_details = get_user_details(token)
    print("User details:", user_details)
else:
    print("Failed to login")


# 실패 테스
token = "faketoken"
user_details = get_user_details(token)
print(user_details)