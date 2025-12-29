from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tool_schema = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "Get system time",
        "parameters": {"type":"object","properties":{}}
    }
}
