from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

class UserUpdateRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, description="Age must be a non-negative integer")

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a non-negative integer")
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a non-negative integer")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    del users[user_id]
    return f"User {user_id} has been deleted"






