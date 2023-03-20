from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return Info.query.filter_by(id=user_id).first()


class Blogger(db.Model):
    __tablename__ = 'blogger'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        
        
   
class Info(db.Model, UserMixin):
    __tablename__ = 'info'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    
    def __init__(self, name, email, password ):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd) 


