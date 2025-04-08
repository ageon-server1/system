from bot_config import ADMINS, RESELLERS

def is_admin(uid): return uid in ADMINS
def is_reseller(uid): return uid in RESELLERS
