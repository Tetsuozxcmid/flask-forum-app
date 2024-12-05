from flask import render_template, request, redirect, url_for,flash
from sqlalchemy import delete
from flask_login import login_user, logout_user, current_user, login_required
from models import User,Room,Comment
from werkzeug.security import generate_password_hash


def register_routes(app, db, bcrypt):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    #new user registration
    @app.route('/signup',methods=['GET','POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            hashed_password = bcrypt.generate_password_hash(password)
            user = User(username=username,password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    #user authorization via session
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter(User.username == username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                    login_user(user)
                    return render_template("index.html")
            else:
                return render_template("500.html"),500

    #user logout via session
    @app.route('/logout',methods=['GET','POST'])
    def logout():
        if current_user.is_authenticated:
            logout_user()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    #new room creating
    @app.route('/createroom',methods=['GET','POST'])
    def create():
        if current_user.is_authenticated:
            name = request.form.get('room_name')
            topic = request.form.get('room_description')
            text = request.form.get('room_text')
            user_id = current_user.uid
            room = Room(room_name=name,room_desc=topic,room_topic=text,user_id=user_id)
            
            db.session.add(room)
            db.session.commit()

            if room:
                
                return render_template('created.html',room=room)
        else:
            return redirect(url_for('login'))
        
    #displaying list of availbale rooms
    @app.route('/rooms',methods=['GET','POST'])
    def show():
        if current_user.is_authenticated:
            username = User.username
            room_name = Room.room_name
            rooms = Room.query.filter(Room.room_name == room_name)
            return render_template('rooms.html',rooms=rooms,username=username)
        return redirect(url_for('signup'))
    
    #displaying certain room 
    @app.route('/room/<int:id>',methods =['GET','POST'])
    def room(id):
        room = Room.query.filter(Room.room_id == id).first()
        comments = db.session.query(Comment.comment_text,User.username,Comment.comment_id,Comment.user_id).join(User).filter(Comment.cooment_room_id==id).all()

        #adding comments 
        if request.method=='POST':
            comm = request.form.get('comment')
            user_id = current_user.uid
            comment = Comment(comment_text = comm,user_id=user_id,cooment_room_id=id)
            db.session.add(comment)
            db.session.commit()
            
            return redirect(url_for('room', id=id))

        return render_template('room.html',room=room,comments=comments)
    
    #other users profile
    @app.route("/user/<username>")
    @login_required
    def user(username):
        user = User.query.filter_by(username=username).first()
        posts = Room.query.filter(Room.user_id == user.uid).all()
        return render_template("user.html",posts=posts,user=user)
    
    #current user profile
    @app.route("/profile/<name>")
    def profile(name):

        if current_user.is_authenticated:

            user = User.query.filter_by(username=name).first()
            posts = Room.query.filter(Room.user_id == user.uid).all()
            return render_template("profile.html",posts=posts,user=user)
        
        return render_template('404.html', 404)

    #deleting room if it belongs to you
    @app.route("/delete-room/<room_id>")
    @login_required
    def delete_room(room_id):

        room = Room.query.filter(Room.room_id == room_id).first()

        db.session.delete(room)
        db.session.commit()
        return redirect(url_for('show'))
    
    #deleting your comment
    @app.route("/delete-comment/<comment_id>")
    @login_required
    def delete_comment(comment_id):
        comment = Comment.query.filter(Comment.comment_id == comment_id).first()
        print(comment)
        db.session.delete(comment)
        db.session.commit()
        
        return render_template("com_deleted.html")
    
    
    
    

    
        
    



