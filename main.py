import openai
import textbase
from textbase.message import Message
from typing import List

# Load your OpenAI API key
openai.api_key = "open AI API KEY"

class InsuranceBot:
    def __init__(self):
        self.user_data = {}

    def get_response(self, message, state):
        message = message.lower()
        response = ""

        if "hi" in message or "hello" in message:
            response = "Hello! Welcome to our Insurance Services. How can I assist you today?"
        elif "car insurance" in message or "buying car insurance" in message:
            response, state = self.ask_car_insurance_plan(state)
        elif "basic plan" in message:
            response = "The Basic plan covers accidental damage and third-party liability with a premium of $300 per year."
        elif "comprehensive plan" in message:
            response = "The Comprehensive plan covers accidental damage, third-party liability, theft, and medical expenses with a premium of $500 per year."
        elif message == "proceed with buying the comprehensive plan":
            response, state = self.get_user_details(state)
        elif "name" in message and "contact number" in message and "vehicle details" in message:
            response = "Thank you! One of our insurance agents will contact you shortly to finalize the purchase. Is there anything else I can assist you with?"
        else:
            # Use OpenAI GPT-3.5 Turbo for generating responses
            response = self.generate_response(message)

        return response, state

    def ask_car_insurance_plan(self, state):
        response = "Sure! We offer two car insurance plans - \"Basic\" and \"Comprehensive.\" "
        response += "The Basic plan covers accidental damage and third-party liability with a premium of $300 per year. "
        response += "The Comprehensive plan covers accidental damage, third-party liability, theft, and medical expenses with a premium of $500 per year. "
        response += "Which plan would you like to know more about?"
        return response, state

    def get_user_details(self, state):
        response = "I can help you with that! To proceed with purchasing the Comprehensive plan, I'll need some details from you. "
        response += "Can you please provide me with your name, contact number, and the vehicle details (make, model, and year of the car)?"
        state["waiting_for_user_details"] = True
        return response, state

    def generate_response(self, message):
        # Use OpenAI GPT-3.5 Turbo to generate response
        bot_response = openai.Completion.create(
            engine="text-davinci-002",  # You can use "text-davinci-002" or "text-gpt-3.5-turbo"
            prompt=message,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            api_key=openai.api_key,
        )

        return bot_response['choices'][0]['text']

# Main script to run the chatbot
bot = InsuranceBot()

@textbase.chatbot("insurance-bot")
def on_message(message_history: List[Message], state: dict = None):
    if state is None:
        state = {}

    user_message = message_history[-1].content
    response, new_state = bot.get_response(user_message, state)

    return response, new_state
