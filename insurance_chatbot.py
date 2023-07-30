class InsuranceChatbot:
    def __init__(self):
        self.insurance_data = {
            "car": {
                "coverage": "Accidental damage, theft, third-party liability",
                "premium": "$500 per year",
            },
            "health": {
                "coverage": "Hospitalization, medical expenses",
                "premium": "$1000 per year",
            },
            # Add more insurance types and their details here
        }

    def get_response(self, message):
        message = message.lower()
        response = ""

        # Simple logic to respond to user queries
        if "hi" in message or "hello" in message:
            response = "Hello! How can I assist you with insurance today?"
        elif "car" in message:
            response = (
                f"Sure! Our car insurance provides coverage for {self.insurance_data['car']['coverage']} "
                f"with a premium of {self.insurance_data['car']['premium']}."
            )
        elif "health" in message or "medical" in message:
            response = (
                f"Absolutely! Our health insurance covers {self.insurance_data['health']['coverage']} "
                f"at a premium of {self.insurance_data['health']['premium']}."
            )
        else:
            response = "I'm sorry, I couldn't understand that. Please ask something else."

        return response
