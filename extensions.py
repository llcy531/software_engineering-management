from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()

## 修改 B3
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