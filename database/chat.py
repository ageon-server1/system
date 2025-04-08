from database.mongo import db

def save_chat(user_id, message):
    db.chats.insert_one({"user_id": user_id, "msg": message})
