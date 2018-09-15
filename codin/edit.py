from flask import Blueprint
from flask import redirect
from flask import request
from flask import render_template
from config import settings
import json
import os

edit_blueprint = Blueprint("ss_edit",__name__,template_folder="templates")

@edit_blueprint.route("/edit",strict_slashes=False,methods=["GET","POST"])
def edit():

    if request.method == "GET":
        name = request.args["username"]
        if name:
            with open(settings.filedata_path, "r", encoding="utf-8") as f:
                for line in f:
                    username, l2tp, password, all = line.split(' ')
                    dic = {}
                    dic['user'] = json.loads(username)
                    dic['password'] = json.loads(password)
                    if name in username:
                        return render_template("edit.html",row=dic)

    if request.method == "POST":
        old_user = request.args["username"]
        user = request.form["user"]
        pwd = request.form["pwd"]

        if old_user:
            with open(settings.filedata_path, encoding='utf-8') as f1, \
                    open(settings.filedata_path_bak, encoding='utf-8', mode='w') as f2:

                for line in f1:
                    username, l2tp, password, all = line.split(' ')
                    if old_user in username:
                        line = '"{}" {} "{}" {}\n'.format(user, 'l2tpd', pwd, '*')

                    f2.write(line)

            os.remove(settings.filedata_path)
            os.rename(settings.filedata_path_bak, settings.filedata_path)

            return redirect("/index/")

    return redirect('/index/')
