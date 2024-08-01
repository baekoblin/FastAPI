import requests

API_URL = "http://localhost:8000"

def get_data(username):
    url = f"{API_URL}/data/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code, response.text

def post_data(username, data):
    url = f"{API_URL}/admin/data?username={username}"
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code, response.text

if __name__ == "__main__":
    # 데이터 읽기 시도
    print("Attempting to read data for 'alice' (admin, user)...")
    result = get_data("alice")
    print("Result:", result)

    print("\nAttempting to read data for 'bob' (user)...")
    result = get_data("bob")
    print("Result:", result)

    print("\nAttempting to read data for 'eve' (guest)...")
    result = get_data("eve")
    print("Result:", result)

    # 데이터 수정 시도
    print("\nAttempting to update data as 'alice'...")
    new_data = {"message": "Hello, world!"}
    result = post_data("alice", new_data)
    print("Result:", result)

    print("\nAttempting to update data as 'bob'...")
    result = post_data("bob", new_data)
    print("Result:", result)
