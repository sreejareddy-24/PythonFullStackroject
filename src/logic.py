from src.db import DatabaseManager

class UserManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add_user(self, name, username, email, password):
        return self.db.create_user(name, username, email, password)

    def list_users(self):
        return self.db.get_all_users()

    def edit_user(self, user_id, name=None, email=None):
        return self.db.update_users(user_id, name=name, email=email)

    def remove_user(self, user_id):
        return self.db.delete_user(user_id)


class DestinationManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add_destination(self, name, country, notes=None, visited=False, photo=None, user_id=None):
        return self.db.create_destination(name, country, notes, visited, photo, user_id)

    def list_all_destinations(self):
        return self.db.get_all_destinations()

    def list_user_destinations(self, user_id):
        return self.db.get_destinations_by_user(user_id)

    def edit_destination(self, destination_id, name=None, country=None, notes=None, visited=None, photo=None):
        return self.db.update_destination(destination_id, name, country, notes, visited, photo)

    def remove_destination(self, destination_id):
        return self.db.delete_destination(destination_id)

    def mark_destination_visited(self, destination_id):
        return self.db.update_destination(destination_id, visited=True)

    def list_visited_destinations(self, user_id):
        resp = self.db.get_destinations_by_user(user_id)
        return [d for d in resp.data] if resp.data else []

    def list_upcoming_destinations(self, user_id):
        resp = self.db.get_destinations_by_user(user_id)
        return [d for d in resp.data if not d.get("visited")] if resp.data else []
