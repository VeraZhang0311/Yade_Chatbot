# 亚德Chatbot配置文件示例
# 将此文件重命名为 config.py 并填入你的API密钥

# 千问API配置
QWEN_API_KEY = "your-qwen-api-key-here"

# 可选的模型配置
# qwen-turbo: 快速响应，适合简单对话
# qwen-plus: 平衡性能，推荐使用
# qwen-max: 最强性能，成本较高
MODEL_NAME = "qwen-plus"

# 对话历史配置
MAX_HISTORY_TURNS = 20  # 保留的最大对话轮次

# API参数配置
API_TEMPERATURE = 0.7  # 控制创造性 (0.0-1.0)
API_TOP_P = 0.8  # 控制多样性 (0.0-1.0)
API_MAX_TOKENS = 1500  # 最大生成token数
