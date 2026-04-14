
from . import API_KEY, LOCAL_LLM, MODEL
import openai
from . import tools


class Summary:
    def __init__(self):
        self._client = openai.OpenAI(base_url=LOCAL_LLM, api_key=API_KEY)
        self._behave = "keep Crutial Information and Summarise"

    def summary(self, input):
        message = [{"role": "assistant", "content": self._behave},
                   {"role": "user", "content": input}]
        response = self._client.chat.completions.create(
            model=MODEL,
            messages=message,
        )
        output = response.choices[0].message.content
        return output


class LLM:
    summariser = Summary()

    def __init__(self):
        self._client = openai.OpenAI(base_url=LOCAL_LLM, api_key=API_KEY)
        self._conversations = {}
        self._behave = "Be nice and talk on point"

    def setBehaviour(self, behave):
        self._behave = behave

    def chat(self, userInput, conversationID):
        # add the unique conversationID to the cache it it's a new chat
        if conversationID not in self._conversations:
            self._conversations[conversationID] = [
                {"role": "system", "content": self._behave}]

        # cache the userInput
        self._conversations[conversationID].append(
            {"role": "user", "content": userInput})

        # Pass the conversation to the LLM
        response = self._client.chat.completions.create(
            model=MODEL,
            messages=self._conversations[conversationID],
            stream=True
        )
        output = ""
        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                output += delta
                yield delta

        if len(output) > 1000:
            # cache the LLM response
            self._conversations[conversationID].append(
                {"role": "assistant", "content": self.summariser.summary(output)})
        else:
            # cache the LLM response
            self._conversations[conversationID].append(
                {"role": "assistant", "content": output})
