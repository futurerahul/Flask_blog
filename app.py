from flask import Flask, render_template
from forms import SignupForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "fSXfzQg6QrS0SNqRcMC1"


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
