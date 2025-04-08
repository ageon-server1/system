async def notify(context, msg, chat_id):
    await context.bot.send_message(chat_id=chat_id, text=msg)
