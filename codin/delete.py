from flask import Blueprint
from flask import redirect
from flask import request
from flask import render_template
from config import settings

delete_blueprint = Blueprint("ss_del",__name__,template_folder="templates")

@delete_blueprint.route("/delete",strict_slashes=False,methods=["GET","POST"])
def delete():

    print('===========================')
    print(request.args["username"])
    name = request.args["username"]
    if name:
        with open(settings.filedata_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open(settings.filedata_path, "w", encoding="utf-8") as f_w:
            for line in lines:
                username, l2tp, password, all = line.split(' ')

                if name in username:
                    continue
                f_w.write(line)

    return redirect('/index/')
