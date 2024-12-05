from app import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<User - {self.username}, Role - {self.role}>'
    
    def get_id(self):
        return self.uid



class Room(db.Model):
    __tablename__ = 'rooms'
    room_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    room_name = db.Column(db.String,nullable=False)
    room_desc = db.Column(db.String,nullable = False)
    room_topic = db.Column(db.String,nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))

    
    def __repr__(self):
        return f'<Room - {self.room_name}, Description - {self.room_desc}>'
    
    def get_id(self):
        return self.room_id
    

class Comment(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    comment_text = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
    cooment_room_id = db.Column(db.Integer,db.ForeignKey('rooms.room_id'))
    


    
    
    def __repr__(self):
        return f'<Comment - {self.comment_text}, id - {self.comment_id}>'
    
    def get_id(self):
        return self.comment_id
        