# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/ocean_farm'
# 1. 密码留空写法（注意冒号后面没有密码）
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/ocean_farm'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

### 修改B2
app = Flask(__name__)
app.config.from_pyfile('config.py')  
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

app.config['JWT_SECRET_KEY'] = 'a9fdg#12!@#A3fFj9z_Secret987' 
jwt = JWTManager(app)  # ✅ 初始化 JWT 管理器
db.init_app(app)

# 使用register_routes函数注册所有路由
register_routes(app)

# 或者，如果你想直接注册蓝图，可以使用以下代码（二选一）
# app.register_blueprint(user_bp)
# app.register_blueprint(datacenter)
# app.register_blueprint(ai)

#修改C4
from flask import Flask
from routes import register_routes
from flask_cors import CORS
from extensions import db
from flask_jwt_extended import JWTManager
from routes.user_routes import user_bp  # 添加这一行
from routes.datacenter import datacenter  # 添加这一行
from routes.ai import ai