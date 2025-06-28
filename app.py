from flask import Flask
from routes import register_routes
from flask_cors import CORS
from extensions import db
from flask_jwt_extended import JWTManager
from routes.user_routes import user_bp  # 添加这一行
from routes.datacenter import datacenter  # 添加这一行
from routes.ai import ai


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

if __name__ == '__main__':
    app.run(debug=True)


### 修改B3
# 创建聊天完成请求，与AI模型进行对话
completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen-plus",  # 使用通义千问Plus模型
    messages=[  # 对话消息列表
        {"role": "system", "content": "你是一个养殖渔场的专家，你会通过天气信息和渔场的水文信息给养殖户智能建议"},  # 系统角色设定，定义AI助手的专业领域和功能
        {"role": "user", "content": "你是谁？"},  # 用户消息，询问AI的身份
    ],
    # Qwen3模型通过enable_thinking参数控制思考过程（开源版默认True，商业版默认False）
    # 使用Qwen3开源版模型时，若未启用流式输出，请将下行取消注释，否则会报错
    # extra_body={"enable_thinking": False},
)
# 打印AI模型的回复内容
print(completion.choices[0].message.content)  # 输出AI助手的回复消息

# 使用register_routes函数注册所有路由
register_routes(app)

# 或者，如果你想直接注册蓝图，可以使用以下代码（二选一）
# app.register_blueprint(user_bp)
# app.register_blueprint(datacenter)
# app.register_blueprint(ai)