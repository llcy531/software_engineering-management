# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/ocean_farm'
# 1. 密码留空写法（注意冒号后面没有密码）
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/ocean_farm'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

### 修改B3
app.config['JWT_SECRET_KEY'] = 'a9fdg#12!@#A3fFj9z_Secret987' 
jwt = JWTManager(app)  # ✅ 初始化 JWT 管理器
db.init_app(app)

# 使用register_routes函数注册所有路由
register_routes(app)

# 或者，如果你想直接注册蓝图，可以使用以下代码（二选一）
# app.register_blueprint(user_bp)
# app.register_blueprint(datacenter)
# app.register_blueprint(ai)

#修改B3
messages=[  # 对话消息列表
        {"role": "system", "content": "你是一个养殖渔场的专家，你会通过天气信息和渔场的水文信息给养殖户智能建议"},  # 系统角色设定，定义AI助手的专业领域和功能
        {"role": "user", "content": "你是谁？"},  # 用户消息，询问AI的身份
    ],
