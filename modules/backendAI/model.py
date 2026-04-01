'''
1. client module to init a AI client - DONE
2. function to generate the data 
3. function to view the data in a pretty format


NOTE: Implement logger, context

future upgrade: Allow important details of the user to be saved locally, which can be used to send it along with the prompt.
'''

from . import API_KEY, LOCAL_LLM, MODEL
import openai

class LLM:
    def __init__(self):
        self._client = openai.OpenAI(base_url=LOCAL_LLM,api_key=API_KEY)
        self._conversations = {}
        self._behave = "Be nice and well spoken"

    # expects the instance of client and a prompt
    def chatWithNoContext(self, instructions, userInput):
        response = self._client.responses.create(model=MODEL,instructions=self._behave,input=userInput)
        return response.output_text
    
    def setBehaviour(self,behave):
        self._behaviour = behave

    def chatWithContext(self, userInput, conversationID):
        if conversationID not in self._conversations:
            self._conversations[conversationID] = []
        self._conversations[conversationID].append({"role": "user", "content": userInput})
        response = self._client.responses.create(model=MODEL,instructions=self._behave,input=self._conversations[conversationID])
        self._conversations[conversationID].append({"role": "assistant", "content": response.output_text})
        return response.output_text


    


