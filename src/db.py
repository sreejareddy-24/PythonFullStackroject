import os
from supabase import create_client, Client
from dotenv import load_dotenv
from passlib.context import CryptContext

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class DatabaseManager:
    # ---------------- Users ----------------
    def create_user(self, name, username, email, password):
        hashed_password = pwd_context.hash(password)
        try:
            return supabase.table("users").insert({
                "name": name,
                "username": username,
                "email": email,
                "password": hashed_password
            }).execute()
        except Exception as e:
            return {"error": str(e)}

    def get_all_users(self):
        try:
            return supabase.table("users").select("*").execute()
        except Exception as e:
            return {"error": str(e)}

    def update_users(self, user_id, name=None, email=None):
        update_data = {}
        if name:
            update_data["name"] = name
        if email:
            update_data["email"] = email
        if not update_data:
            return None
        try:
            return supabase.table("users").update(update_data).eq("id", user_id).execute()
        except Exception as e:
            return {"error": str(e)}

    def delete_user(self, user_id):
        try:
            return supabase.table("users").delete().eq("id", user_id).execute()
        except Exception as e:
            return {"error": str(e)}

    # ---------------- Destinations ----------------
    def create_destination(self, name, country, notes=None, visited=False, photo=None, user_id=None):
        try:
            return supabase.table("destinations").insert({
                "name": name,
                "country": country,
                "notes": notes,
                "visited": visited,
                "photo": photo,
                "user_id": user_id
            }).execute()
        except Exception as e:
            return {"error": str(e)}

    def get_all_destinations(self):
        try:
            return supabase.table("destinations").select("*").execute()
        except Exception as e:
            return {"error": str(e)}

    def get_destinations_by_user(self, user_id):
        try:
            return supabase.table("destinations").select("*").eq("user_id", user_id).execute()
        except Exception as e:
            return {"error": str(e)}

    def update_destination(self, dest_id, name=None, country=None, notes=None, visited=None, photo=None):
        update_data = {}
        if name: update_data["name"] = name
        if country: update_data["country"] = country
        if notes: update_data["notes"] = notes
        if visited is not None: update_data["visited"] = visited
        if photo: update_data["photo"] = photo
        if not update_data:
            return None
        try:
            return supabase.table("destinations").update(update_data).eq("id", dest_id).execute()
        except Exception as e:
            return {"error": str(e)}

    def delete_destination(self, dest_id):
        try:
            return supabase.table("destinations").delete().eq("id", dest_id).execute()
        except Exception as e:
            return {"error": str(e)}

    def mark_destination_visited(self, dest_id):
        try:
            return supabase.table("destinations").update({"visited": True}).eq("id", dest_id).execute()
        except Exception as e:
            return {"error": str(e)}
