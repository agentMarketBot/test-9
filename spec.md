# Test Message Exchange Specification

## Summary
This specification defines a simple message exchange system that allows sending and receiving messages between participants.

## Components

### Message
A message contains the following properties:
- sender: String identifier of the message sender
- content: String content of the message
- timestamp: Optional timestamp of when the message was sent

### MessageExchange
The main class that handles message operations:

#### Methods
1. send_message(sender: str, content: str) -> Message
   - Creates and stores a new message
   - Returns the created message object

2. get_messages() -> list[Message]
   - Returns a copy of all stored messages
   - Does not modify the original message list

3. clear_messages()
   - Removes all stored messages
   - Used for cleanup and testing purposes

## Implementation
The specification is implemented in Python with the following files:
- message_exchange.py: Core implementation
- test_message_exchange.py: Unit tests verifying the functionality

Fixes #1
