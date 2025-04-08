from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot_config import BOT_TOKEN
from handlers import core_commands, key_handler, chatgpt_handler

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("run", core_commands.run))
    app.add_handler(CommandHandler("addvps", core_commands.add_vps))
    app.add_handler(CommandHandler("removevps", core_commands.remove_vps))
    app.add_handler(CommandHandler("status", core_commands.status))
    app.add_handler(CommandHandler("resources", core_commands.resources))
    app.add_handler(CommandHandler("help", core_commands.help_command))

    app.add_handler(CommandHandler("genkey", key_handler.gen_key))
    app.add_handler(CommandHandler("rckey", key_handler.rc_key))
    app.add_handler(CommandHandler("redeemr", key_handler.redeem_reseller))
    app.add_handler(CommandHandler("balancekey", key_handler.balance_key))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_handler.chat_reply))

    app.run_polling()

if __name__ == "__main__":
    main()
