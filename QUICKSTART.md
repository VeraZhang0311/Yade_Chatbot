# 亚德Chatbot - 快速入门指南

## 5分钟快速开始

### 第一步：安装依赖

```bash
pip install requests
```

### 第二步：获取API密钥

1. 访问 https://dashscope.aliyun.com/
2. 注册/登录阿里云账号
3. 进入控制台 → 创建应用 → 获取API Key

### 第三步：配置密钥

打开 `yade_chatbot.py`，找到这一行（第444行左右）：

```python
API_KEY = "your-qwen-api-key-here"
```

替换为你的实际密钥：

```python
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
```

### 第四步：运行

```bash
python yade_chatbot.py
```

### 第五步：开始对话

```
你: 你好
亚德: 你好。我是亚德，一个旅行者。

你: 最近有点想家
亚德: 你说的让我想起离开家的那个清晨...
```

## 特殊命令

在对话中输入：

- `quit` 或 `exit` - 退出对话
- `save` 或 `保存` - 保存对话记录
- `summary` 或 `摘要` - 查看对话统计

## 触发故事的示例对话

**触发亲情故事：**
```
你: 我好想我爸妈
```

**触发爱情故事：**
```
你: 我和前任分手了，很遗憾
```

**触发友情故事：**
```
你: 我的朋友都渐行渐远了
```

**触发事业故事：**
```
你: 我工作很迷茫，不知道方向
```

**触发健康故事：**
```
你: 我最近生病了
```

## 常见问题

**Q: 如何更换模型？**

修改初始化参数：
```python
chatbot = YadeChatbot(
    api_key=API_KEY,
    model="qwen-max"  # 可选: qwen-turbo, qwen-plus, qwen-max
)
```

**Q: 对话记录保存在哪？**

在程序运行目录下，文件名格式：`yade_conversation_20240127_103000.json`

**Q: 如何修改角色设定？**

编辑 `yade_chatbot.py` 中的 `SYSTEM_PROMPT` 变量（第11行开始）

**Q: 如何添加更多故事？**

在系统提示词的"五个核心故事"部分添加新故事，按照相同格式

## 目录结构

```
yade_chatbot/
├── yade_chatbot.py              # 主程序
├── config_example.py            # 配置文件示例
├── PARAMETER_TUNING_GUIDE.md    # 调参指南 控制对话风格
├── README.md                    # 详细文档
└── QUICKSTART.md                # 本文件
```

## 下一步

- 阅读 `README.md` 了解完整功能
- 运行 `yade_chatbot` 体验聊天
- 体验 Character.AI 了解同类产品
- 思考如何添加游戏剧情推进功能

## 反馈

如有问题或建议，欢迎反馈！

---

**愿风雪记得你的名字。**
