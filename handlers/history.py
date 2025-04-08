# Optional chat history save per user
chat_history = {}

def save_message(user_id, message):
    if user_id not in chat_history:
        chat_history[user_id] = []
    chat_history[user_id].append(message)

def get_history(user_id):
    return chat_history.get(user_id, [])
