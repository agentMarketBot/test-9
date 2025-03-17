class Message:
    def __init__(self, sender: str, content: str):
        self.sender = sender
        self.content = content
        self.timestamp = None

class MessageExchange:
    def __init__(self):
        self.messages = []
    
    def send_message(self, sender: str, content: str) -> Message:
        message = Message(sender, content)
        self.messages.append(message)
        return message
    
    def get_messages(self) -> list[Message]:
        return self.messages.copy()
    
    def clear_messages(self):
        self.messages.clear()