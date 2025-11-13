# 🎯 Interview & Resume Coach Chatbot

Hi! This is Zabeer Safwan. I have created this **AI-powered chatbot** which is designed to help users with **resume building**, **interview preparation**, and **placement guidance**.  
It acts as a **personal career coach**, giving helpful, conversational responses to any question related to interviews or resumes.

---

## 🚀 Features

- 💬 **Interactive Chat UI** built with Streamlit  
- 🧠 **Powered by Ollama (local LLM)** — no internet API needed  
- 📝 Helps with:
  - Resume writing tips
  - Common interview questions and answers
  - Placement and HR advice
  - Behavioral and situational interview guidance
- ⚡ Lightweight, runs locally on your machine

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Streamlit** (for web interface)
- **Ollama** (for LLM-based responses)
- **LangChain** (optional: for better conversation flow)
- **GitHub** (for version control & submission)

---

## 🧠 How It Works

1. The user asks any question about **interviews**, **resumes**, or **placements**.  
2. The chatbot sends the question to **Ollama’s local model** (like Llama 3, Mistral, etc.).  
3. The model returns a detailed and context-aware answer.  
4. Streamlit displays the conversation in a chat-like interface.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this Repository

git clone https://github.com/TheTribalChief20/interview-chatbot-app.git
cd interview-chatbot-app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Ollama (make sure it’s installed)
You can download Ollama from: https://ollama.ai
Then pull a model (e.g. Llama 3):
ollama pull llama3

4️⃣ Run the chatbot
streamlit run interview_chatbot_ollama.py
