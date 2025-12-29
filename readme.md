# 🤖 Agentic Assistant (Tool-Calling AI)

A function-calling agent built using Groq LLMs.
It supports:
- Checking time
- Fetching weather
- Generating QR codes
- Writing to files

## 🚀 How to Run
```bash
python app.py
``` 


# 🤖 Agentic Assistant — AI Tool-Calling Agent

This project is a **function-calling AI agent** that uses LLMs (e.g., Groq / LLaMA) to perform real-world tasks like:

- Getting current time
- Fetching weather from IP
- Writing text files
- Generating QR codes with logos

All actions are done through a controlled **agent loop** with single tool execution per turn.

---

## 🚀 Features

✔️ Dynamic tool routing  
✔️ Loop safety (no infinite tool calls)  
✔️ Structured tool responses  
✔️ ReAct-style flow (Think → Act → Observe → Answer)  
✔️ Modular architecture

---

## 🧠 Example Commands

| Input | What Happens |
|--------|---------------|
| `What time is it?` | Calls time tool |
| `Save the weather into weather.txt` | weather → write file |
| `Make a QR code for https://google.com using logo.jpg` | generate QR pic |

---

## 🏗 Architecture

LLM → Tool Call → Execute → Inject Result → LLM → Final Answer

---

## 🔧 Setup

```bash
git clone https://github.com/mayank61/agentic-assistant
cd agentic-assistant
pip install -r requirements.txt
python app.py



