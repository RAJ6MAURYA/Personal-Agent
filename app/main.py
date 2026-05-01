from contextlib import asynccontextmanager
from service.backendAI.model import initLlm
import service.database as database
from routes.chat import chat
from fastapi import FastAPI
import uvicorn
import os

MODEL = os.getenv("MODEL", "llama3.2")


@asynccontextmanager
async def lifespan(app: FastAPI):
    initLlm(MODEL)
    # connectDb()
    yield
    # disconnectDb()

app = FastAPI(
    title="Personal Agent",
    lifespan=lifespan
)


app.include_router(router=chat)


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, host="127.0.0.1")
