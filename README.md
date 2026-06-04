# 🌍 GeoIntel AI Assistant

🚀 A real-time, LLM-powered City Intelligence Assistant that delivers **weather updates**, **live news insights**, and **AI-generated responses** using tool-augmented agents built with Mistral AI, LangChain, and Streamlit.

---

## 📌 Overview

GeoIntel AI Assistant is an intelligent conversational system that combines **Large Language Models (LLMs)** with external tools to provide **real-world, up-to-date information**.

Unlike traditional chatbots, it can:
- Fetch real-time weather data 🌦️
- Retrieve latest news updates 📰
- Reason intelligently using LLM agents 🤖
- Use external APIs via tool-calling architecture ⚙️

---

## ✨ Features

- 🌦️ **Real-Time Weather Intelligence** using OpenWeather API  
- 📰 **Live News Retrieval** using Tavily Search API  
- 🤖 **LLM Agent System** powered by Mistral AI  
- 🧠 **Tool-Augmented Reasoning** via LangChain Agents  
- 💬 **Conversational UI** built with Streamlit  
- 🔁 **Session-based Chat Memory** for context-aware interactions  
- ⚡ **Error-safe API handling & structured outputs**

---

## 🏗️ Architecture


---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – UI framework
- **LangChain** – Agent orchestration
- **Mistral AI** – LLM backend
- **Tavily API** – Web search / news retrieval
- **OpenWeather API** – Weather data
- **dotenv** – Environment variable management
- **Requests** – API communication

---

## 📂 Project Structure

```
```
## ⚙️ Setup Instructions

1️⃣ Clone the repository
git clone https://github.com/your-username/geo-intel-ai-assistant.git
cd geo-intel-ai-assistant

```
```
## 2️⃣ Create virtual environment
python -m venv venv

Activate:

Windows:
venv\Scripts\activate

```
```
## 3️⃣ Install dependencies
pip install -r requirements.txt
```
```

## 4️⃣ Add environment variables

Create a .env file:

OPENWEATHER_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key

```

```
## 5️⃣ Run the app
streamlit run app.py
