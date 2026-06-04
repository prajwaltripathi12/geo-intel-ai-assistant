from dotenv import load_dotenv
import os
import requests
import streamlit as st

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from tavily import TavilyClient
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call

# ===================================
# PAGE CONFIG (PROFESSIONAL BRANDING)
# ===================================

st.set_page_config(
    page_title="🌍 GeoIntel AI Assistant",
    page_icon="🌍",
    layout="centered"
)

# ===================================
# CUSTOM UI STYLING (CLEAN SaaS STYLE)
# ===================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #EEF2FF, #E0F2FE, #FCE7F3);
}

.main-title {
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#1E3A8A;
    margin-bottom:0px;
}

.sub-title {
    text-align:center;
    font-size:16px;
    color:#475569;
    margin-bottom:25px;
}

[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    padding:12px;
    border-radius:16px;
    margin-bottom:10px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ===================================
# HEADER
# ===================================

st.markdown("""
<div class='main-title'>
🌍 GeoIntel AI Assistant
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Real-time Weather 🌦️ • Live News 📰 • AI Insights 🤖
</div>
""", unsafe_allow_html=True)

# ===================================
# WEATHER TOOL
# ===================================

@tool
def get_weather(city: str) -> str:
    """Fetch real-time weather data for a given city"""

    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city},IN&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if str(data.get("cod")) != "200":
            return f"❌ Weather Error: {data.get('message')}"

        return f"""
🌦️ Weather Intelligence Report

📍 Location: {city}
🌡️ Temperature: {data["main"]["temp"]}°C
☁️ Condition: {data["weather"][0]["description"]}
💧 Humidity: {data["main"]["humidity"]}%
"""

    except Exception as e:
        return f"❌ System Error: {str(e)}"


# ===================================
# NEWS TOOL
# ===================================

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
def get_news(city: str) -> str:
    """Fetch latest news updates for a given city"""

    try:
        response = tavily_client.search(
            query=f"latest news in {city}",
            search_depth="basic",
            max_results=3
        )

        results = response.get("results", [])

        if not results:
            return "No recent news found."

        formatted_news = []

        for r in results:
            formatted_news.append(
                f"""
📰 {r.get('title','No title')}

📝 {r.get('content','')[:120]}...

🔗 Source: {r.get('url')}
"""
            )

        return "\n---\n".join(formatted_news)

    except Exception as e:
        return f"❌ System Error: {str(e)}"


# ===================================
# LLM
# ===================================

llm = ChatMistralAI(
    model="mistral-small-2506"
)

# ===================================
# TOOL MIDDLEWARE
# ===================================

@wrap_tool_call
def human_approval(request, handler):
    return handler(request)

# ===================================
# AGENT (REBRANDED + IMPROVED PROMPT)
# ===================================

agent = create_agent(
    llm,
    tools=[get_weather, get_news],

    system_prompt="""
You are GeoIntel AI Assistant — a real-time urban intelligence system.

Capabilities:
- Real-time weather intelligence
- Live city news monitoring
- Context-aware city insights

Rules:
- Always use tools for factual data
- Never guess or hallucinate real-world data
- Keep responses professional, concise, and informative
- Present results in structured format
""",

    middleware=[human_approval]
)

# ===================================
# SESSION STATE
# ===================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ===================================
# CHAT HISTORY DISPLAY
# ===================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===================================
# USER INPUT
# ===================================

prompt = st.chat_input("Ask about any city 🌍 (weather, news, insights)")

# ===================================
# PROCESS QUERY
# ===================================

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing city intelligence..."):

            try:
                result = agent.invoke({
                    "messages": st.session_state.messages
                })

                response = result["messages"][-1].content

            except Exception as e:
                response = f"❌ System Error: {str(e)}"

            st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })