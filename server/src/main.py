from fastapi import FastAPI, WebSocket
import os
from chat import ChatManager

app = FastAPI()
chat = ChatManager()

@app.on_event("shutdown")
async def chat_shutdown():
    del chat

@app.websocket("api/chat")
async def get_response(websocket: WebSocket):
    await websocket.accept()
    while True:
        user_message = await websocket.received_text()
        print(f"Received message from user: {user_message}")
        for assistant_message in chat.talk(user_message):
            print(f"Received message from AI: {assistant_message}.")
            await websocket.send_text(assistant_message)

