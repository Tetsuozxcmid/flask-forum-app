Project Overview
----------------------
This project is Flask based forum with webchat using Sockets,web application where you can authenticate, create discussion rooms, post comments, view the profiles of other users.  

### Installation
  ```python 
      python -m venv venv #creating venv for Windows
      python3 -m venv venv #creating venv for MacOS/Linux
      ---------------
      venv/scripts/activate # windows
      source venv/bin/activate # macOS/Linux

      pip install -r requirements.txt #installing packages
      py run.py #running app and creating instance folder
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

 ### Authentication Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/signup` | GET, POST | Register a new user |
| `/login` | GET, POST | Authenticate and log in |
| `/logout` | GET, POST | Log out the user |

### Room Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/createroom` | POST | Create a new room |
| `/rooms` | GET | List all available chat rooms |
| `/room/<int:id>` | GET, POST | View a specific chat room and add a comment |
| `/delete-room/<room_id>` | GET | Delete a chat room if authorized |

### Profile Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/user/<username>` | GET | View another user's profile |
| `/profile/<name>` | GET | View current user's profile |

### Comment Routes
### Profile Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/delete-comment/<comment_id>` | GET | Delete a comment if authorized |




  
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
