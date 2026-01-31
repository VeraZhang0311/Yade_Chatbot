# 亚德(Yade) Chatbot - AI角色对话系统

基于千问大语言模型的角色扮演chatbot，实现了一个来自涅夫海湾的旅行者——亚德。

## 功能特点

### 1. 角色一致性
- 完整的人物设定（性格、背景、说话风格）
- 精心设计的系统提示词，确保角色行为一致
- 温和克制的对话风格，符合亚德的性格设定

### 2. 情感共鸣机制
- **5个核心故事**，覆盖人生五大主题：
  - 亲情：《冰湾的最后一夜》
  - 爱情：《短暂的温度》
  - 友情：《不会变老的约定》
  - 事业：《不被需要的地图》
  - 健康：《魔力枯竭的七日》

- **智能触发机制**：
  - 通过关键词自动识别话题
  - 根据情绪强度决定分享深度
  - 首次分享简短版本，追问时展开细节
  - 避免重复讲述已分享的故事

### 3. 对话记忆管理
- 保存完整对话历史（内存存储）
- 自动限制历史长度，防止token超限
- 支持导出对话记录为JSON格式
- 追踪已分享的故事，避免重复

### 4. 交互功能
- 实时命令行对话界面
- 特殊命令支持：
  - `quit/exit`: 退出对话
  - `save/保存`: 保存对话记录
  - `summary/摘要`: 查看对话统计

## 安装依赖

```bash
pip install requests
```

## 快速开始

### 1. 配置API密钥

打开 `yade_chatbot.py`，找到 `main()` 函数，修改：

```python
def main():
    API_KEY = "your-qwen-api-key-here"  # 替换为你的千问API密钥
    # ...
```

### 2. 运行程序

```bash
python yade_chatbot.py
```

## 使用示例

### 基础对话

```
你: 你好，你是谁？
亚德: 你好。我是亚德，一个来自涅夫海湾的旅行者。

你: 最近有点想家了
亚德: 你说的让我想起离开家的那个清晨。母亲给了我一条亲手编织的围巾，
     内侧绣着"愿风雪记得你的名字"。我至今都没舍得用它。
```

### 深入对话

```
你: 我和朋友渐行渐远了，很难过
亚德: 我明白那种感觉...我有个人类朋友叫里昂。二十年后重逢时，
     他说他老了，我却没变。

你: 后来怎么样了？
亚德: 我第一次主动拥抱了他，告诉他："时间或许改变了你的容貌，
     但没有改变你在我心中的位置。"
```

## 代码结构

```
yade_chatbot.py
├── SYSTEM_PROMPT          # 系统提示词（角色设定 + 5个故事）
├── ConversationMemory     # 对话记忆管理类
│   ├── add_message()      # 添加消息到历史
│   ├── get_messages_for_api()  # 获取API调用格式
│   ├── save_to_file()     # 保存对话记录
│   └── get_conversation_summary()  # 获取对话摘要
├── QwenAPI                # 千问API封装类
│   └── chat()             # 调用API进行对话
└── YadeChatbot            # 主聊天机器人类
    ├── chat()             # 处理单次对话
    └── start_interactive_session()  # 启动交互会话
```

## API说明

### YadeChatbot 类

```python
# 初始化
chatbot = YadeChatbot(
    api_key="your-api-key",
    model="qwen-plus"  # 可选: qwen-turbo, qwen-plus, qwen-max
)

# 单次对话
response = chatbot.chat("你好")

# 启动交互式会话
chatbot.start_interactive_session()

# 获取对话记录对象
memory = chatbot.get_memory()
```

### ConversationMemory 类

```python
# 获取对话摘要
summary = memory.get_conversation_summary()
# 返回: {
#     "total_turns": 10,
#     "message_count": 20,
#     "shared_stories": ["冰湾的最后一夜"],
#     "start_time": "2024-01-27T10:30:00"
# }

# 导出对话历史
json_str = memory.export_history()

# 保存到文件
memory.save_to_file("conversation_20240127.json")
```

## 触发机制说明

故事会根据用户输入中的关键词自动触发：

| 主题 | 关键词示例 | 触发故事 |
|------|--------|----------|
| 亲情 | 家人、父母、思念、离别 | 《冰湾的最后一夜》 |
| 爱情 | 喜欢、恋爱、分手、遗憾 | 《短暂的温度》 |
| 友情 | 朋友、陪伴、疏远 | 《不会变老的约定》 |
| 事业 | 工作、迷茫、转变 | 《不被需要的地图》 |
| 健康 | 生病、照顾、身体 | 《魔力枯竭的七日》 |

## 获取千问API密钥

1. 访问 [阿里云百炼平台](https://dashscope.aliyun.com/)
2. 注册/登录账号
3. 创建应用，获取API Key
4. 新用户通常有免费额度可用

## 常见问题

**Q: API调用失败怎么办？**  
A: 检查API密钥是否正确，网络是否畅通，余额是否充足。

**Q: 如何添加更多故事？**  
A: 在系统提示词的"五个核心故事"部分按相同格式添加即可。

**Q: 对话记录存在哪里？**  
A: 目前只存在内存中，使用 `save` 命令可导出到JSON文件。

## 技术特性

### 优点
- 简单直接：单LLM方案，无需额外组件
- 响应快速：无RAG检索延迟
- 上下文连贯：AI能全局理解所有故事
- 易于维护：所有逻辑在一个文件中

### 限制
- 适合5-15个故事（更多建议用RAG）
- 系统提示词约3500 tokens
- 只保留最近20轮对话（可配置）

---

**愿风雪记得你的名字。**
