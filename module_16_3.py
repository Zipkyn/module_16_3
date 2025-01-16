from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def add_user(
    username: Annotated[
        str, Path(title="Введите имя пользователя", min_length=5, max_length=20, examples={"example": "UrbanUser"})
    ],
    age: Annotated[
        int, Path(title="Введите возраст", ge=18, le=120, examples={"example": 24})
    ]
):

    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"Пользователь {new_id} зарегистрирован"}

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[
        str, Path(title="Введите ID пользователя", examples={"example": "1"})
    ],
    username: Annotated[
        str, Path(title="Введите имя пользователя", min_length=5, max_length=20, examples={"example": "UrbanProfi"})
    ],
    age: Annotated[
        int, Path(title="Введите возраст", ge=18, le=120, examples={"example": 28})
    ]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"Пользователь {user_id} обновлен"}

@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[
        str, Path(title="Введите ID пользователя", examples={"example": "2"})
    ]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    del users[user_id]
    return {"message": f"Пользователь {user_id} удален"}

@app.get("/user/{user_id}")
def get_user(
    user_id: Annotated[
        int, Path(title="Введите ID пользователя", ge=1, le=100, examples={"example": 1})
    ]
):
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"user_id": user_id, "details": users[user_id_str]}

@app.get("/user/{username}/{age}")
def get_user_by_name_and_age(
    username: Annotated[
        str, Path(title="Введите имя пользователя", min_length=5, max_length=20, examples={"example": "UrbanUser"})
    ],
    age: Annotated[
        int, Path(title="Введите возраст", ge=18, le=120, examples={"example": 24})
    ]
):
    return {"username": username, "age": age}







