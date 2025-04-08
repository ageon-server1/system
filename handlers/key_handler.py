from telegram import Update
from telegram.ext import ContextTypes
from database.models import generate_key, get_key_balance, redeem_key
from utils.role_check import is_admin, is_reseller

async def gen_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_reseller(update.effective_user.id):
        return
    hours, userlimit = map(int, context.args)
    key = generate_key(hours, userlimit)
    await update.message.reply_text(f"🗝️ Key:\n`{key}`", parse_mode="Markdown")

async def rckey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    balance = get_key_balance(update.effective_user.id)
    await update.message.reply_text(f"💳 Balance: {balance}")

async def redeem_reseller(update: Update, context: ContextTypes.DEFAULT_TYPE):
    key = context.args[0]
    msg = redeem_key(update.effective_user.id, key)
    await update.message.reply_text(msg)

async def balance_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    await update.message.reply_text("✅ Balance logic placeholder set.")
