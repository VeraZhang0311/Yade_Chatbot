"""
亚德聊天室 - Streamlit Web 界面
"""

import streamlit as st
from yade_chatbot import YadeChatbot

# 页面配置
st.set_page_config(
    page_title="亚德聊天室",
    page_icon="🎭",
    layout="centered"
)

# 标题
st.title("🎭 亚德聊天室")
st.caption("与来自涅夫海湾的旅行者对话")


def get_api_key():
    """获取API密钥：优先从Streamlit secrets，否则从环境变量"""
    import os
    # Streamlit Cloud secrets
    try:
        if "QWEN_API_KEY" in st.secrets:
            return st.secrets["QWEN_API_KEY"]
    except Exception:
        pass
    # 环境变量
    return os.environ.get("QWEN_API_KEY", "")


def init_chatbot():
    """初始化聊天机器人实例（每个用户独立）"""
    if "chatbot" not in st.session_state:
        api_key = get_api_key()
        if not api_key:
            return None
        st.session_state.chatbot = YadeChatbot(api_key=api_key, model="qwen-plus")
    return st.session_state.chatbot


def init_messages():
    """初始化消息历史"""
    if "messages" not in st.session_state:
        # 添加亚德的开场白
        st.session_state.messages = [
            {"role": "assistant", "content": "你好。我是亚德，一个旅行者。"}
        ]


# 检查API密钥
api_key = get_api_key()
if not api_key:
    st.error("请配置 QWEN_API_KEY")
    st.info("在 Streamlit Cloud 的 Secrets 中添加：\n```\nQWEN_API_KEY = \"你的API密钥\"\n```")
    st.stop()

# 初始化
chatbot = init_chatbot()
init_messages()

# 显示历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧑" if message["role"] == "user" else "🎭"):
        st.markdown(message["content"])

# 用户输入
if prompt := st.chat_input("输入消息..."):
    # 显示用户消息
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 获取亚德的回复
    with st.chat_message("assistant", avatar="🎭"):
        with st.spinner("亚德正在思考..."):
            response = chatbot.chat(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# 侧边栏
with st.sidebar:
    st.markdown("### 关于亚德")
    st.markdown("""
    - 种族：精灵族与魔兽族混血
    - 年龄：101岁（约等于人类26岁）
    - 职业：旅行者、诗人、记录者
    - 家乡：涅夫海湾
    """)

    st.markdown("---")

    # 清空对话按钮
    if st.button("🔄 开始新对话"):
        st.session_state.messages = [
            {"role": "assistant", "content": "你好。我是亚德，一个旅行者。"}
        ]
        # 重新初始化chatbot以清空记忆
        if "chatbot" in st.session_state:
            del st.session_state.chatbot
        st.rerun()

    st.markdown("---")
    st.caption("对话次数：" + str(len([m for m in st.session_state.messages if m["role"] == "user"])))
