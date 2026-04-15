import random
import json

def handle_tools_call(message):
    response = []
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_names":
            arguments = json.loads(tool_call.function.arguments)
            start_name = arguments.get("start_name")
            name = get_names(start_name=start_name)
            response.append({
                "role": "tool",
                "content": name,
                "tool_call_id": tool_call.id
            })
    print("handle_tools_call response",response)
    return response


def get_names(start_name=None):
    names = ["simran", "raj", "pragathi", "chethan", "swapnil", "luckshami"]

    if start_name:
        filtered = [name for name in names if name.lower().startswith(start_name)]
        if filtered:
            return random.choice(filtered)
        return f"No names found starting with '{start_name}'."
            
    return random.choice(names)


name_function = {
    "name": "get_names",
    "description": "Suggest a random name only when the user asks for a name suggestion.",
    "parameters": {
        "type": "object",
        "properties": {
            "start_name": {
                "type": "string",
                "description": "Optional starting letter(s) to filter suggested names.",
            }
        },
        "additionalProperties": False
    }
}


tools = [{"type": "function","function":name_function}]
