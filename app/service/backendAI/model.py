import os
import openai
from . import _tools
import pprint
import ollama
import sys

_llmClient = None

API_KEY = os.getenv("API_KEY","")
LOCAL_LLM =os.getenv("LOCAL_LLM","http://localhost:11434/v1")
MODEL= os.getenv("MODEL","llama3.2")


# It ensures the selected local LLM is available 
def initLlm(model):
    response = ollama.list()
    available = [m.model.split(":")[0] for m in response.models]
    if model not in available:
        try:
            for progress in ollama.pull(model,stream=True):
                completed = progress.completed
                total = progress.total
                if isinstance(completed,int) and isinstance(total,int) and total > 0:
                    percentage = (completed/total) * 100
                    print(f'\r{progress.status}: {percentage:6.2f}% completed',end="",flush=True)
                if progress.status == "success":
                    print("completed pulling")
        except Exception as e:
            print(f"\nFailed to download the Model: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"{LLM} already available to use")
    _llmClient = LLM()

class Summary:
    def __init__(self):
        self._client = openai.OpenAI(base_url=LOCAL_LLM, api_key=API_KEY)
        self._behave = "Summarise the following text in under 400 characters. Keep only the most crucial information. Be concise."

    def summary(self, text):
        message = [{"role": "system", "content": self._behave},
                   {"role": "user", "content": text}]
        response = self._client.chat.completions.create(
            model=MODEL,
            messages=message,
        )
        output = response.choices[0].message.content
        return output


class LLM:
    summariser = Summary()

    def __init__(self, _system_prompt=""):
        self._client = openai.OpenAI(base_url=LOCAL_LLM, api_key=API_KEY)
        self._system_prompt = _system_prompt or "Be nice and talk on point. Use the tools only when required and never output like JSON tool calls. Also only reply to the last message and other messages are for context"
        self._history = []

    def _sentToLLM(self, message):
        temp = "The Previous messages are only for context, Just answer to this question ONLY ->"
        messages = [{"role": "system", "content": self._system_prompt}] + [{"role": h["role"], "content": h["content"]} for h in self._history] + [{"role": "user", "content": temp+message}]
        self._history.append({"role": "user", "content": message})
        response = self._client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=_tools.tools,
            tool_choice="auto"
        )
        while response.choices[0].finish_reason == "tool_calls":
            message = response.choices[0].message
            tool_response = tools.handle_tools_call(message=message)
            messages.append(message)
            messages.extend(tool_response)
            response = self._client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=_tools.tools
            )

        output = response.choices[0].message.content
        if len(output) > 500:
            self._history.append({"role": "assistant", "content": self.summariser.summary(output)})
        return output

    def chat(self, message):
        output = self._sentToLLM(message)
        with open("conversation.txt", "w") as f:
            print("HISTORY", self._history, file=f,end="\n")
        return output
