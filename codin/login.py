from flask import Blueprint
from flask import Flask, render_template, request, redirect, session
from config import settings
import os
app = Flask(__name__, template_folder='templates')

login_blueprint = Blueprint("ss_login", __name__, template_folder="templates")

print(settings.userinfo_path)
print(os.path.exists(settings.userinfo_path))
def auth(username, password):
    with open(settings.userinfo_path, encoding='utf-8', ) as f1:
        for line in f1:
            line = line.strip()
            if not line == '':
                user, pwd = line.split("|")
                if username == user and password == pwd:
                    return True


@login_blueprint.before_request
def process_request():
    if request.path == "/login":
        return None
    if not session.get("userinfo"):
        return redirect("/login")
    return None


@app.route("/login", methods=["GET", "POST"])
@login_blueprint.route("/login", strict_slashes=False, methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get("user")
        print(username)
        password = request.form.get("pwd")

        res = auth(username, password)
        if res:
            session["userinfo"] = username

            return redirect("/index")
        else:

            return render_template("login.html", msg="用户名或者密码错误")
