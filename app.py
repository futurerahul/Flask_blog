from typing import DefaultDict
from flask import Flask, render_template
from forms import SignupForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "fSXfzQg6QrS0SNqRcMC1"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    posts = db.relationship("Post", backref="user", lazy=True)

    def __repr__(self):
        return f"User({self.username}, {self.email})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    comments = db.relationship("Comment", backref="post", lazy=True)

    def __repr__(self):
        return f"Posts({self.id}, {self.user_id}, {self.date_posted})"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)

    def __repr__(self):
        return f"Comment({self.id}, {self.user_id}, {self.post_id}, {self.date_posted})"


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template("signup.html", title="Signup", form=form)


@app.route("/login")
def login():
    form = SignupForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
