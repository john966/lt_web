import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
filedata_dir = os.path.join(BASE_DIR,"data")  #读取您的文件目录


filedata_path=os.path.join(filedata_dir,"chap-secrets")  # 配置文件

filedata_path_bak = os.path.join(filedata_dir,"chap-secrets.bak")  # 备份配置文件 (修改的时候需要使用请一定要与配置文件名称一样)

userinfo_path = os.path.join(filedata_dir,"userinfo")  # 用户文件
