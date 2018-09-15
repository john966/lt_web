from flask import Blueprint
from flask import redirect
from flask import request
from flask import render_template


add_blueprint = Blueprint("ss_add",__name__,template_folder="templates")

@add_blueprint.route("/add",strict_slashes=False,methods=["GET","POST"])
def add():
    if request.method == "GET":

        return render_template("add.html")

    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]

    with open('./data/chap-secrets', encoding='utf-8') as f1, \
            open('./data/chap-secrets', encoding='utf-8', mode='a') as f2:
        try:
            for line in f1:
                print(line)
                username, l2tp, password, all = line.split(' ')

                if not user == username:

                    print(username,user)

            f2.write('"{}" {} "{}" {}\n'.format(user,'l2tpd',pwd,'*'))


            return redirect("/index")

        except Exception as e:
            print(e)
            hint = '<script>alert("添加失败！");window.location.href="/index/"</script>'
        return hint
