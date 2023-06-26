from fastapi import FastAPI, WebSocket
import os
from chat import ChatManager

app = FastAPI()
chat = ChatManager()

@app.onevent("shutdown")
async def chat_shutdown():
    del chat

@app.websocket("/chat")
async def get_response(websocket: WebSocket):
    await websocket.accept()
    while True:
        for message in chat.talk("It's late at night")
            print(message)
            await websocket.send_text(message)

