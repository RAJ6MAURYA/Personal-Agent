
from . import API_KEY, LOCAL_LLM, MODEL
import openai

class Summary:
    def __init__(self):
        self._client = openai.OpenAI(base_url=LOCAL_LLM, api_key=API_KEY)
        self._behave = "keep Crutial Information and Summarise"

    
    def summary(self,input):
        response = self._client.responses.create(
            model=MODEL,
            instructions=self._behave,
            input=input
        )
        output = response.output_text
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
            self._conversations[conversationID] = []

        # cache the userInput
        self._conversations[conversationID].append(
            {"role": "user", "content": userInput})

        # Pass the conversation to the LLM
        response = self._client.responses.create(
            model=MODEL,
            instructions=self._behave,
            input=self._conversations[conversationID],
            stream=True)

        for event in response:
            if event.type == "response.output_text.delta":
                yield event.delta
        
        # full response
        output = event.response.output[0].content[0].text
        if len(output) > 1000:
            # cache the LLM response
            self._conversations[conversationID].append(
                {"role": "assistant", "content": self.summariser.summary(output)})
        else:
            # cache the LLM response
            self._conversations[conversationID].append(
                {"role": "assistant", "content": output})
