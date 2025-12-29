import json
from models.client import call_llm
from agent.system_prompt import SYSTEM_PROMPT
from agent.router import dispatch_tool
from config.settings import MAX_TURNS, MAX_HISTORY
from tools import schemas  # automatically gather all schemas
tools = schemas.TOOLS



def run_agent(user_input):
    messages = [{"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}]
    for _ in range(MAX_TURNS):
        
        response = call_llm(messages, tools)

        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            print("🎯 Result:", msg.content)
            return msg.content

        tc = msg.tool_calls[0]
        name = tc.function.name
        args = json.loads(tc.function.arguments or "{}")

        result = dispatch_tool(name, args)

        messages.append({
            "role":"tool",
            "tool_call_id": tc.id,
            "content": result
        })

    print("⚠️ Max turns reached.")
