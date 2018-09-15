from flask import Flask
from codin import login
from codin import index
from codin import add
from codin import delete
from codin import edit
from codin import logout

def create_app():
    app = Flask(__name__)

    app.register_blueprint(login.login_blueprint)

    app.register_blueprint(index.index_blueprint)
    app.register_blueprint(add.add_blueprint)
    app.register_blueprint(delete.delete_blueprint)
    app.register_blueprint(edit.edit_blueprint)

    app.register_blueprint(logout.logout_blueprint)

    return app