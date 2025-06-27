from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()

## 修改 B2
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/ocean_farm'
# 1. 密码留空写法（注意冒号后面没有密码）
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/ocean_farm'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True