from pydantic import BaseModel, field_validator
from typing import List


class User(BaseModel):
    name: str
    age: int

    @field_validator('age')
    def check_age(cls, v):
        if v < 18:
            raise ValueError("Age Must be at least 18")
        return v
    

class Item(BaseModel):
    name: str
    price: int

class Order(BaseModel):
    id: int 
    items: List[Item]


user_obj = User(name = "he", age = 21)

order = Order(id = 12, items = [{"name":"Apple","price":100}])