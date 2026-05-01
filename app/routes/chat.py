from fastapi import APIRouter
from .schemas import RequestChat, ResponseChat


chat = APIRouter(prefix="/chat")


@chat.post("/",
           response_model=ResponseChat
           )
async def hello_world(req: RequestChat):
    print(req.message)
    return ResponseChat(message="hi RAJ")
