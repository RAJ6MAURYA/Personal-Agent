from modules.backendAI import model


client = model.LLM()

for chunk in client.chat(userInput='hi i am raj maurya', conversationID="2"):
	print(chunk,flush=True, end="")

for chunk in client.chat(userInput='what\'s my name', conversationID="2"):
	print(chunk,flush=True, end="")

