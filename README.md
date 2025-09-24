# MyTravelBook

My Travel Book is a full-stack web app that lets users create a personal travel bucket list, track visited destinations, and store notes or photos. It features user authentication, CRUD for destinations, and optional map integration to visualize travels.

# Features

User Accounts: Sign up and log in to create a personal travel book.
Manage your destinations securely under your account.

Add Destinations: Save dream destinations with name, country, and notes.
Optionally upload photos to capture memories.

Track Travel Progress: Mark destinations as “Visited” or “Want to Visit.”
Easily keep track of your travel goals.

Organized Views: View destinations in separate sections for visited and upcoming trips.
Quickly navigate between places you’ve been and places to explore.

Optional Map Integration: See all your destinations on a map using Google Maps or Leaflet.js.
Visualize your travels geographically for a better overview.

CRUD Operations: Edit or delete destinations whenever needed.
Maintain and update your travel list easily.

## project Structure 
MyTravelBook/
|
|---src/                # core application logic
|    |--logic.py        # business logic and task
operations
|    |_db.py            # Database operations
|
|---api/                # Backend API
|    |_main.py          # FastAPI endpoints
|
|---frontend/           # Frontend Application
|    |_app.py           # Streamlit web interface
|
|___requirements.txt    #python dependencies 
|
|___README.md           #python Documentation
|
|___.env                #python variables  

## Quick Start

### Prerequisites

 - Python 3.8 or higher
 - A supabase account
 - Git(Push,cloning)

### 1. Clone or Download the project
# Option 1: Clone with Git
git clone <repositry-url>

# option 2: Download and extract the ZIP file 

### 2. Install Dependencies 

# Install all required Python packages
pip install -r requirements.txt

### 3. Set up supabase Database

1.Create a supabase Project:

2.Create the users table
 - go to the sql editor in your supabase dashboard
 -run this sql command:

 ---sql
 create table users(
  id serial primary key,
  name text,
  username text unique not null,
  email text unique not null,
  password text not null
);

---