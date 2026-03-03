def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "hey bro, you are my god!👾"
    
    elif "praise me" in user_input:
        return "you are my god the supreme legend!👾"
    
    elif "bye" or "see ya later" in user_input:
        return "No problem, hope your dbz kakarot loads well😉"

    else:
        return "hmm.... i still foolish, no problem you will eventually teach me my lord!(⌐■_■)."

print("god father of chatgpt,MY chatbot.\n")

while True:
    user_message = input("you: ")

    response = chatbot_response(user_message)
    print("bot:", response)
    
    if "bye" in user_message.lower():
        break
                