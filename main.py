from modules.backendAI import model


client = model.LLM()
print(client.chatWithContext(userInput='hi i am raj maurya',conversationID="2"))
print(client.chatWithContext(userInput='what\'s my name',conversationID="2"))
