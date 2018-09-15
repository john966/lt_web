from config import create_app
from flask import Flask,request,redirect,session
from datetime import timedelta
import os

flask_app = create_app()

flask_app.config ['SECRET_KEY'] = os.urandom(24) #每一次服务器启动后，SECRET_KEY(盐)不一样
flask_app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  #配置过期时间

@flask_app.before_request
def is_login():  # 判断是否登录
    # 白名单设置,判断为登录页面时
    if request.path == "/login":
        # 跳过处理
        return None
    # 判断session是不存在时
    if not session.get("userinfo"):
        # 重定向到登录页面
        return redirect("/login")


if __name__ == '__main__':
    flask_app.run("0.0.0.0",8000,debug=True)