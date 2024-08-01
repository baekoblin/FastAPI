def process_user(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid data format")
    
    name = data.get("name")
    age = data.get("age")
    