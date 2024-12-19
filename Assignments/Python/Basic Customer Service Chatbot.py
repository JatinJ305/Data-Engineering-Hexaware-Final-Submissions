import random

# Predefined knowledge base
FAQ = {
    "What is your return policy?": "You can return items within 30 days of purchase.",
    "How can I track my order?": "Use the tracking link sent to your email after the order is shipped.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, and PayPal."
}

# Troubleshooting tips
TROUBLESHOOTING = {
    "I can't login": "Try resetting your password or check if Caps Lock is on.",
    "My payment was declined": "Ensure your card details are correct or contact your bank."
}

# Greeting and handling input
def greet_user():
    print("Hello! Welcome to our customer service chatbot. How can I assist you today?")

def get_response(user_input):
    for question, answer in FAQ.items():
        if question.lower() in user_input.lower():
            return answer
    for issue, solution in TROUBLESHOOTING.items():
        if issue.lower() in user_input.lower():
            return solution
    return "I'm sorry, I don't have the answer to that. Please contact our support team."

def chatbot():
    greet_user()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye', 'quit']:
            print("Chatbot: Thank you for contacting us! Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
