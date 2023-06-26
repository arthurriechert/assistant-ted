import os
import openai
from dotenv import load_dotenv
import json

class ChatManager:

    def __init__ (self):
        print(f"Initializing OpenAI API")
        load_dotenv()
        self.llm = openai
        self.llm.api_key = os.getenv("OPENAI_API_KEY")
        self.chat_history = []
        self.settings = {}

        if not os.path.exists("chat_history.json"):
            with open("chat_history.json", "w") as file:
                json.dump([{"role": "system", "content": "You are an AI named Ted. Answer the user to the best of your abilities"}], file)
        
        with open("chat_history.json", "r") as file:
            self.chat_history = json.load(file)

        if not os.path.exists("chat_settings.json"):
            with open("chat_settings.json", "w") as file:
                json.dump({
                    "temperature": 0.7,
                    "max_tokens": 8192,
                    "model": "gpt-4-0613"}, 
                    file)
        
        with open("chat_settings.json", "r") as file:
            self.settings = json.load(file)

    def __repr__ (self):
        return self.chat_history[-1].value

    def __getitem__ (self, index):
        return self.chat_history[index]

    def __add__ (self, message: dict):
        self.chat_history.append(message)
        return self.chat_history

    def __del__ (self):
        with open("chat_history.json", 'w') as file:
            json.dump(self.chat_history, file)

    def talk (self, user_message: str) -> str:
        chat = self + {"role": "user", "content": user_message}
        response = openai.ChatCompletion.create(
                model=self.settings["model"],
                temperature=self.settings["temperature"],
                messages=chat,
                stream=True
        )
        self += {"role": "assistant", "content": ""}
        for chunks in response:
            chunk = chunks["choices"][0]["delta"]
            try:
                self[-1]["content"] += chunk["content"]
                yield chunk["content"]
            except KeyError:
                break
