import requests

base_url = "http://127.0.0.1:8000"

def get_items():
    response = requests.get(f"{base_url}/items")
    return response.json()

def print_items(title, items):
    print(f"\n{title}: \n", items)

def test_get_items():
    items_before = get_items()
    print_items("Before GET Request", items_before)

    response = requests.get(f"{base_url}/items")

    print("GET Response: ", response.status_code, response.json())

    items_after = get_items()

    print_items("After GET Request", items_after)

def test_create_time():
    items_before = get_items()
    print_items("Before POST Request", items_before)

    response = requests.post(f"{base_url}/items/3", data ={"name": "Notebook"})
    print("POST Response:", response.status_code, response.json())

    items_after = get_items()
    print_items("After POST Request", items_after)


def test_update_item():
    items_before = get_items()
    print_items("Before Put Request", items_before)

    response = requests.put(f"{base_url}/items/1", data = {"name": "Updated Pen"})
    print("PUT Response: ", response.status_code, response.json())

    items_after = get_items()
    print_items("After PUT Request", items_after)


def test_delete_item():
    items_before = get_items()
    print_items("Before DELETE Request", items_before)

    response = requests.delete(f"{base_url}/items/2")
    print("DELETE Response", response.status_code, response.json())

    items_after = get_items()
    print_items("After Delete Request", items_after)


def test_patch_item():
    items_before = get_items()
    print_items("Before PATCH Request", items_before)

    response = requests.patch(f"{base_url}/items/1", data = {"name": "Patched Pen"})
    print("PATCH Response:", response.status_code, response.json())

    items_after = get_items()
    print_items("After PATCH Request", items_after)


test_get_items()
test_create_time()
test_update_item()
test_delete_item()
test_patch_item()