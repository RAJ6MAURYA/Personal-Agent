from modules.backendAI import model


client = model.LLM()

prompt = input("enter a Prompt: ")
while prompt != "exit":
	response = client.chat(message=prompt)
	print(response)
	print(end="\n \n")
	prompt = input("Prompt: ")



