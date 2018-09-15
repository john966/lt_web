from flask import Blueprint
from flask import Flask,render_template,request,redirect,session
app = Flask(__name__,template_folder='templates')


logout_blueprint = Blueprint("ss_logout",__name__,template_folder="templates")

@logout_blueprint.route("/logout",strict_slashes=False,methods=["GET","POST"])
def logout():
    session.get("userinfo")
    session.clear() #清除所有session

    return redirect('/login')