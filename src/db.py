import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Create user
def create_user(name, username, email, password):
    return supabase.table("users").insert({
        "name": name,
        "username": username,
        "email": email,
        "password": password
    }).execute()

# Get all users
def get_all_users():
    return supabase.table("users").select("*").execute()

# Update user
def update_users(id, name=None, email=None):
    update_data = {}
    if name:
        update_data["name"] = name
    if email:
        update_data["email"] = email
    if update_data:
        return supabase.table("users").update(update_data).eq("id", id).execute()
    return None

# Delete user
def delete_user(id):
    return supabase.table("users").delete().eq("id", id).execute()

# Create destination
def create_destination(name, country, notes=None, visited=False, photo=None, user_id=None):
    return supabase.table("destinations").insert({
        "name": name,
        "country": country,
        "notes": notes,
        "visited": visited,
        "photo": photo,
        "user_id": user_id
    }).execute()

# Get all destinations
def get_all_destinations():
    return supabase.table("destinations").select("*").execute()

# Get destinations by user
def get_destinations_by_user(user_id):
    return supabase.table("destinations").select("*").eq("user_id", user_id).execute()

# Update destination
def update_destination(id, name=None, country=None, notes=None, visited=None, photo=None):
    update_data = {}
    if name:
        update_data["name"] = name
    if country:
        update_data["country"] = country
    if notes:
        update_data["notes"] = notes
    if visited is not None:
        update_data["visited"] = visited
    if photo:
        update_data["photo"] = photo

    if update_data:
        return supabase.table("destinations").update(update_data).eq("id", id).execute()
    return None

# Delete destination
def delete_destination(id):
    return supabase.table("destinations").delete().eq("id", id).execute()

# Mark destination as visited
def mark_destination_visited(id):
    return supabase.table("destinations").update({"visited": True}).eq("id", id).execute()

# Get only visited destinations by user
def get_visited_destinations(user_id):
    return supabase.table("destinations").select("*").eq("user_id", user_id).eq("visited", True).execute()

# Get only upcoming (not visited) destinations by user
def get_upcoming_destinations(user_id):
    return supabase.table("destinations").select("*").eq("user_id", user_id).eq("visited", False).execute()
