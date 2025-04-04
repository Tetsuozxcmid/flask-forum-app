from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from flask_socketio import SocketIO

db = SQLAlchemy()
login_manager = LoginManager()  
bcrypt = Bcrypt()  

def create_app():
    app = Flask(__name__, template_folder='templates',static_folder='static')  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./forum_app.db'
    app.secret_key = 'SOME KEY'
    db.init_app(app)
    login_manager.init_app(app)  
    socketio = SocketIO(app)
    from models import User
    
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))
    
    bcrypt.init_app(app)  

    from routes import register_routes
    register_routes(app, db, bcrypt,socketio)

    migrate = Migrate(app, db,render_as_batch=True)

    return app
