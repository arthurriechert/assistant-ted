from chat import ChatManager

if __name__ == "__main__":
    chat = ChatManager()
    for message in chat.talk("I am an alien"):
        print(message)
    del chat
