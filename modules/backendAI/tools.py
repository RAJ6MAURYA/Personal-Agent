import random

def get_names():
    names = ["simran","raj","pragathi","chethan","swapnil","luck"]
    print("Get the tools call get_names")
    return names[random.randint(0, len(names) - 1)]


name_function = {
    "name": "get_names",
    "description": "Get a random name from the list",
    "parameters": {
        "type": "object",
        "properties": {
            "start_name": {
                "type": "string",
                "description": "Starting letter with which user wants the name to start with",
            }
        },
        "required": ["start_name"],
        "additionalProperties": False
    }
}


tools = [{"type": "function","function":name_function}]
