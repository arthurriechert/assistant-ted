from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import os
from chat import ChatManager

app = FastAPI()

origins = [
        "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/api/chat")
async def get_response(websocket: WebSocket):
    await websocket.accept()
    chat = ChatManager()
    while True:
        user_message = await websocket.receive_text()
        print(f"Received message from user: {user_message}")
        await websocket.send_text("/~~")
        for assistant_message in chat.talk(user_message):
            await websocket.send_text(assistant_message)

        await websocket.send_text("~~/")

@app.websocket("/api/ws/test")
async def get_test_response(websocket: WebSocket):
    await websocket.accept()
    while True:
        test_message = await websocket.receive_text()
        print(f"Received test message: {test_message}")
        await websocket.send_text(f"Received your test message: {test_message}")
