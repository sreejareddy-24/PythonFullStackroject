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

3. **Get your credentials:

### 4. Configure Environoment Variables

1.Create a '.env' file in the project root

2. Add your supabse credentials to '.env:
SUPABASE_URL =your_project_url_here
SUPABASE_KEY=your_anon_key_here

**Example**
SUPABASE_URL="https://icixultfsegggdmvjvae.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImljaXh1bHRmc2VnZ2dkbXZqdmFlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI0ODAsImV4cCI6MjA3MzY1ODQ4MH0.-TMKAZGLJ26-okzSw0lHdxaQvsZ_z6MWtWMwxtB1toQ"

### 5. Run the application

## Streamlit Frontend
streamlit run frontend/app.py

the app will open in your browser at 'http://localhost:8501'

## FastAPI Backend

cd API
python main.py

The API will be available at 'http://localhost:8000'

## How to use

## Technical Details

### Technologies Used 

- **Frontend**:Streamlit (Python web framework)
- **Backend**:FastAPI (python REST API framework)
- **Database**:Supabase (PostrgreSQL - based backend-as-a-service)
- **Language**: Python 3.8+

### Key Components

1. **'src/db.py'**:Database operations 
  - Handle all CRUD operations with supabase

2. **'src/logic.py'**:Business logic 
  -Task validation and processing


## Troubleshooting 

## Common Issues

1. **Module not found" errors**
  -mke sure tou've installed all dependecied: 'pip install -r requirements.txt'
  -check that tou're running commands from the correct directory 

## Future Enhancements

ideas foe extending this project:

## Support 

if you encounter any issues or have questions :
sreeja.reddy0524@gmail.com
9381224396