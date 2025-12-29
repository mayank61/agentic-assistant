from tools.time_tools import get_current_time
from tools.weather_tools import get_weather_from_ip
from tools.qr_tools import generate_qr_code
from tools.file_tools import write_txt_file

TOOL_REGISTRY = {
    "get_current_time": get_current_time,
    "get_weather_from_ip": get_weather_from_ip,
    "generate_qr_code": generate_qr_code,
    "write_txt_file": write_txt_file
}

def dispatch_tool(name, args):
    fn = TOOL_REGISTRY.get(name)
    if not fn:
        raise ValueError(f"Unknown tool: {name}")
    return fn(**args) if args else fn()
