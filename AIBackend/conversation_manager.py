class ConversationManager:
    def __init__(self, assistant1, assistant2):
        self.assistant1 = assistant1
        self.assistant2 = assistant2
        self.conversation = []

    def start_conversation(self, initial_message, turns=5):
        self.conversation.append({"role": "user", "content": initial_message})

        for _ in range(turns):
            current_assistant = self.assistant1 if len(self.conversation) % 2 == 0 else self.assistant2
            response = current_assistant.generate_response(self.conversation)
            print(f"{current_assistant.name}: {response}")
            self.conversation.append({"role": "assistant", "content": response})