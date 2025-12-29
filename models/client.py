from groq import Groq
from config.settings import MODEL_NAME
from dotenv import load_dotenv
import os
load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
def call_llm(messages, tools):
    return client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools
    )
