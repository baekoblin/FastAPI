import requests

BASE_URL = "http://127.0.0.1:8000/users"

def get_users():
    response = requests.get(f"{BASE_URL}/")
    return response.json()

def create_user(name, age):
    response = requests.post(BASE_URL + "/", json={"name": name, "age": age})
    return response.json()

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    return response.json()

def update_user(user_id, name, age):
    response = requests.put(f"{BASE_URL}/{user_id}", json={"name": name, "age": age})
    return response.json()

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    return response.json()

# 예시 사용법
print("Get users:", get_users())
new_user = create_user("John Doe", 30)
print("Create user:", new_user)
user_id = new_user['id']
print("Get user:", get_user(user_id))
print("Update user:", update_user(user_id, "John Updated", 31))
print("Delete user:", delete_user(user_id))
