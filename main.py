from modules.backendAI import model


client = model.LLM()

prompt = input("enter a Prompt: ")
while prompt != "exit":
	for chunk in client.chat(userInput=prompt, conversationID="2"):
		print(chunk,flush=True, end="")
	print(end="\n \n")
	prompt = input("Prompt: ")



