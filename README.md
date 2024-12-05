Project Overview
----------------------
This project is Flask based forum web application where you can authenticate, create discussion rooms, post comments, view the profiles of other users.  

### Instalation
  ```python 
      py -m venv venv #creating venv
      venv/scripts/activate #activating venv
      pip install -r requirements.txt #installing packages
      py run.py #running app 
      flask db upgrade #adding models in db
  ```
  
    
----------------------


### Features

1. User Authentication
   - Sign Up: Users can create an secure account with a username and password
    - Passwords are securely hashed using Werkzeug and bcrypt
   - Login: Users can log into account
   - Logout: Users can log out from their session
2. Profiles
  - Your profile with information about your posts
  - Every user got a profile page, where you can see rooms they created
  
3. Room Management
  - Create Rooms: Authenticated users can create chat rooms with a name,description       and topic
  - View Rooms: Authenticated users can view a list of available chat rooms and choose them for chatting
  - Room Detais: Users can see a details of the room such as - comments, topic, name of the room
  -   Managing: Users could delete rooms which are belongs them
  
4.  Comment system
  - Posting comments in chat rooms
  - Delete comments which are belongs them
5. Access control
  - Restricted access to content such as rooms, commenting, and profile viewing to authenticated users only
  - Redirects unauthenticated users to the login page
  
Tech part
----------------------
Backend

- Flask: web framework
- Flask-Login: Manages user session and authentication
- SQLAlchemy: ORM for db
- bcrypt: Hashes password for storage in db

Frontend

- Bootstrap
- HTML/CSS

Database

- SQLite: Replaceable with any SQL-supported database
