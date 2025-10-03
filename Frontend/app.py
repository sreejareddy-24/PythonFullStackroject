import streamlit as st
import requests

# Backend URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="My Travel Book", page_icon="✈️", layout="wide")

st.title("🌍 My Travel Book")
st.write("Manage your travel destinations and user accounts.")

# -----------------------------
# USER MANAGEMENT
# -----------------------------
st.sidebar.header("👤 User Management")

menu = st.sidebar.radio("Choose Section:", ["Users", "Destinations"])

# -----------------------------
# Users Section
# -----------------------------
if menu == "Users":
    st.subheader("User Management")

    # Create User
    with st.form("create_user"):
        st.write("### Create a New User")
        name = st.text_input("Name")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Create User")

        if submitted:
            data = {"name": name, "username": username, "email": email, "password": password}
            response = requests.post(f"{API_URL}/users", json=data)
            if response.status_code == 200:
                st.success("✅ User created successfully!")
            else:
                st.error(f"❌ Error: {response.text}")

    # Show all users
    st.write("### Registered Users")
    resp = requests.get(f"{API_URL}/users")
    if resp.status_code == 200:
        # Ensure the response is a dictionary with a 'data' key
        json_resp = resp.json()
        if isinstance(json_resp, dict):
            users = json_resp.get("data", [])
        else:
            # If API returns a list directly
            users = json_resp

        # Ensure each user is a dictionary
        users_dict = [u if isinstance(u, dict) else {} for u in users]

        if users_dict:
            st.table([{"ID": u.get("id"), "Name": u.get("name"), "Username": u.get("username")} for u in users_dict])
        else:
            st.info("No users found.")
    else:
        st.error("Failed to fetch users.")


# -----------------------------
# Destinations Section
# -----------------------------
if menu == "Destinations":
    st.subheader("Destinations Management")

    # Select user
    resp = requests.get(f"{API_URL}/users")
    if resp.status_code == 200:
        users = resp.json().get("data", [])
        user_options = {u["name"]: u["id"] for u in users} if users else {}
    else:
        users = []
        user_options = {}

    selected_user = st.selectbox("Select User", list(user_options.keys())) if user_options else None

    if selected_user:
        user_id = user_options[selected_user]

        # Add Destination
        with st.form("create_destination"):
            st.write("### Add a New Destination")
            name = st.text_input("Destination Name")
            country = st.text_input("Country")
            notes = st.text_area("Notes")
            visited = st.checkbox("Visited?")
            photo = st.text_input("Photo URL (optional)")
            submitted = st.form_submit_button("Add Destination")

            if submitted:
                data = {
                    "name": name,
                    "country": country,
                    "notes": notes,
                    "visited": visited,
                    "photo": photo,
                    "user_id": user_id
                }
                response = requests.post(f"{API_URL}/destinations", json=data)
                if response.status_code == 200:
                    st.success("✅ Destination added successfully!")
                else:
                    st.error(f"❌ Error: {response.text}")

        # Show User Destinations
        st.write(f"### {selected_user}'s Destinations")
        resp = requests.get(f"{API_URL}/destinations/user/{user_id}")
        if resp.status_code == 200:
            destinations = resp.json().get("data", [])
            if destinations:
                for d in destinations:
                    st.markdown(f"**{d.get('name')}** ({d.get('country')})")
                    st.write(f"Notes: {d.get('notes')}")
                    st.write(f"Visited: {'✅ Yes' if d.get('visited') else '❌ No'}")
                    if d.get("photo"):
                        st.image(d.get("photo"), width=200)
                    st.divider()
            else:
                st.info("No destinations added yet.")
        else:
            st.error("Failed to fetch destinations.")
