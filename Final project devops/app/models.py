from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# users table
class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

#post
class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"
