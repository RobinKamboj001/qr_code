import random

# Dictionary of predefined responses
responses = {
    "hello": ["Hello! 😊", "Hi there! 👋", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great! 🤖", "I'm fine! What about you?", "Feeling awesome!"],
    "your name": ["I'm a chatbot! You can call me ChatGPT. 😊", "I am your friendly chatbot!"],
    "bye": ["Goodbye! 👋", "See you later! 😊", "Take care!"],
    "default": ["I'm not sure how to respond to that. 🤔", "Can you please ask something else?", "Sorry, I don't understand."]
}

# Function to get chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Chatbot conversation loop
print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("🤖 Chatbot:", random.choice(responses["bye"]))
        break
    print("🤖 Chatbot:", chatbot_response(user_input))
