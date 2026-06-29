
from chatbot.model import ChatbotModel

class ChatBot:
    def __init__(self):
        self.model = ChatbotModel()

    def get_response(self, user_input):
        intent = self.model.predict(user_input)
        if intent == "greeting":
            return "Hello! How can I help you?"
        elif intent == "farewell":
            return "Bye! Have a great day."
        elif intent == "thanks":
            return "You’re welcome!"
        else:
            return "Sorry, I didn’t understand that."
