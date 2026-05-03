from fastapi import APIRouter, HTTPException
from .schemas import RequestChat, ResponseChat
from service.backendAI import model


chat = APIRouter(prefix="/chat")


@chat.post("/",
           response_model=ResponseChat
           )
def hello_world(req: RequestChat):
    if model.llmClient is None:
        raise HTTPException(status_code=503, detail="LLM client is not initialized")

    message = req.message
    response = model.llmClient.chat(message=message)
    return ResponseChat(message=response)
