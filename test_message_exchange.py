import unittest
from message_exchange import MessageExchange, Message

class TestMessageExchange(unittest.TestCase):
    def setUp(self):
        self.exchange = MessageExchange()
    
    def test_send_message(self):
        message = self.exchange.send_message("Alice", "Hello, World!")
        self.assertEqual(message.sender, "Alice")
        self.assertEqual(message.content, "Hello, World!")
        self.assertEqual(len(self.exchange.get_messages()), 1)
    
    def test_get_messages(self):
        self.exchange.send_message("Alice", "First message")
        self.exchange.send_message("Bob", "Second message")
        messages = self.exchange.get_messages()
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].content, "First message")
        self.assertEqual(messages[1].sender, "Bob")
    
    def test_clear_messages(self):
        self.exchange.send_message("Alice", "Test message")
        self.exchange.clear_messages()
        self.assertEqual(len(self.exchange.get_messages()), 0)

if __name__ == '__main__':
    unittest.main()