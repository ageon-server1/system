from database.mongo import db
import uuid

def generate_key(hours, limit):
    key = str(uuid.uuid4()).split('-')[0]
    db.keys.insert_one({"key": key, "hours": hours, "limit": limit})
    return key

def get_key_balance(uid):
    return db.keys.count_documents({"used_by": uid})

def redeem_key(uid, key):
    data = db.keys.find_one({"key": key})
    if not data: return "❌ Invalid key"
    db.keys.update_one({"key": key}, {"$set": {"used_by": uid}})
    return "✅ Key redeemed!"

def add_vps(ip, user, passwd):
    db.vps.insert_one({"ip": ip, "user": user, "pass": passwd})

def remove_vps(ip):
    db.vps.delete_one({"ip": ip})

def list_resources():
    return "CPU: 80%, RAM: 70%"
