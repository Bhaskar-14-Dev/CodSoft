import re
import random
import datetime

# Greeting keywords and responses
GREETING_KEYWORDS = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
GREETING_RESPONSES = [
    "Hello! How can I help you today?",
    "Hi there! What can I do for you?",
    "Hey! Need travel advice?",
    "Greetings! How may I assist you?"
]

# Farewell keywords and responses
FAREWELL_KEYWORDS = ['bye', 'goodbye', 'see you', 'exit', 'quit']
FAREWELL_RESPONSES = [
    "Goodbye! Have a wonderful day.",
    "See you next time!",
    "Bye! Safe travels!",
    "It was nice chatting with you."
]

def get_time_of_day():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    else:
        return "evening"

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    for word in GREETING_KEYWORDS:
        if word in user_input:
            tod = get_time_of_day()
            return f"{random.choice(GREETING_RESPONSES)} Good {tod}!"

    # Farewell
    for word in FAREWELL_KEYWORDS:
        if word in user_input:
            return random.choice(FAREWELL_RESPONSES)

    # Asking about chatbot's name
    if "your name" in user_input or "who are you" in user_input:
        return "I'm TravelBot, your friendly travel assistant!"

    # Asking about time or date
    if "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}."
    if "date" in user_input or "day" in user_input:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."

    # Asking about weather
    if re.search(r'\bweather\b', user_input):
        return "I can't check the weather yet, but I can help you plan your trip!"

    # Asking about travel destinations
    if "recommend" in user_input or "suggest" in user_input:
        return ("I recommend visiting Paris for its rich culture, Bali for beautiful beaches, "
                "or New York for a vibrant city experience. Where would you like to go?")

    # Asking for help
    if "help" in user_input or "options" in user_input:
        return ("I can help you with:\n"
                "- Destination recommendations\n"
                "- Basic travel advice\n"
                "- Telling you the time or date\n"
                "- General greetings\n"
                "Just type your question!")

    # General fallback
    return "Sorry, I didn't understand that. Can you ask something else or type 'help' for options?"

print("="*45)
print("TravelBot: Hi! I'm your travel assistant chatbot.")
print("Type 'help' to see what I can do. Type 'bye' to exit.")
print("="*45)
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("TravelBot:", response)
    if any(farewell in user_input.lower() for farewell in FAREWELL_KEYWORDS):
        break