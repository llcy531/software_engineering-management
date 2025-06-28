import os
# 导入OpenAI客户端库，用于与AI模型进行交互
from openai import OpenAI


# 创建OpenAI客户端实例，配置阿里云百炼API
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-b6bb661e82b94e96ba90d7c5bb09ca44",  # 阿里云百炼API密钥，用于身份验证
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里云百炼API的兼容模式基础URL
)

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

#修改C4
import os
# 导入OpenAI客户端库，用于与AI模型进行交互
from openai import OpenAI