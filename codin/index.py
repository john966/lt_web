from flask import Blueprint
from flask import redirect,render_template
from config import settings
import json

index_blueprint = Blueprint("ss_b",__name__,template_folder="../templates",static_folder="../templates/statics",static_url_path="/templates/statics")

print(settings.filedata_path)


@index_blueprint.route("/index",strict_slashes=False,methods=["GET","POST"])
def index():

    in_lst=[]
    with open(settings.filedata_path, encoding='utf-8') as f1:

        for line in f1:
            dic = {}
            user, l2tp, pwd, all = line.split(' ')

            dic = {"user":json.loads(user),"pwd":json.loads(pwd)}
            in_lst.append(dic)

    return render_template("index.html",s_list=in_lst)

