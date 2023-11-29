from assistant import Assistant
from conversation_manager import ConversationManager

def main():

    assistant1 = Assistant("assistant-1", "I am a friendly and enthusiastic AI.")
    assistant2 = Assistant("assistant-2", "I am a thoughtful and analytical AI.")

    conversation_manager = ConversationManager(assistant1, assistant2)
    conversation_manager.start_conversation("Hello, how are you?")

if __name__ == "__main__":
    main()
