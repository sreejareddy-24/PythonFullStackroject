from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import UserManager, DestinationManager

app = FastAPI(title="Student Task Manager API", version="1.0")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_manager = UserManager()
destination_manager = DestinationManager()

# ------------------- Models -------------------
class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: str = None
    email: EmailStr = None

class DestinationCreate(BaseModel):
    name: str
    country: str
    notes: str = None
    visited: bool = False
    photo: str = None
    user_id: int

class DestinationUpdate(BaseModel):
    name: str = None
    country: str = None
    notes: str = None
    visited: bool = None
    photo: str = None

# ------------------- Endpoints -------------------
@app.get("/")
def home():
    return {"message": "Student Task Manager API is running"}

# Users
@app.get("/users")
def get_users():
    resp = user_manager.list_users()
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

@app.post("/users")
def create_user(user: UserCreate):
    resp = user_manager.add_user(user.name, user.username, user.email, user.password)
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    resp = user_manager.edit_user(user_id, name=user.name, email=user.email)
    return {"success": True, "data": resp.data if resp and hasattr(resp, "data") else None}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    resp = user_manager.remove_user(user_id)
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

# Destinations
@app.get("/destinations")
def get_all_destinations():
    resp = destination_manager.list_all_destinations()
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

@app.get("/destinations/user/{user_id}")
def get_user_destinations(user_id: int):
    resp = destination_manager.list_user_destinations(user_id)
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

@app.post("/destinations")
def create_destination(dest: DestinationCreate):
    resp = destination_manager.add_destination(
        dest.name, dest.country, dest.notes, dest.visited, dest.photo, dest.user_id
    )
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

@app.put("/destinations/{dest_id}")
def update_destination(dest_id: int, dest: DestinationUpdate):
    resp = destination_manager.edit_destination(
        dest_id, name=dest.name, country=dest.country, notes=dest.notes, visited=dest.visited, photo=dest.photo
    )
    return {"success": True, "data": resp.data if resp and hasattr(resp, "data") else None}

@app.delete("/destinations/{dest_id}")
def delete_destination(dest_id: int):
    resp = destination_manager.remove_destination(dest_id)
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

@app.put("/destinations/{dest_id}/mark-visited")
def mark_destination_visited(dest_id: int):
    resp = destination_manager.mark_destination_visited(dest_id)
    return {"success": True, "data": resp.data if hasattr(resp, "data") else resp}

@app.get("/destinations/{user_id}/visited")
def list_visited_destinations(user_id: int):
    return {"success": True, "data": destination_manager.list_visited_destinations(user_id)}

@app.get("/destinations/{user_id}/upcoming")
def list_upcoming_destinations(user_id: int):
    return {"success": True, "data": destination_manager.list_upcoming_destinations(user_id)}