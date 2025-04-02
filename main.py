from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI() # create an instance of fastAPI

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None #this field can be optional / none

users_db = []


@app.get("/users/", response_model=List[User])
def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/user/", response_model=User)
def create_user(user: User):
    for existing_user in users_db:
        if existing_user.email == user.email:
          raise HTTPException(status_code=404, detail="Email is already registered!")  
        
    users_db.append(user)
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            del users_db[index]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")