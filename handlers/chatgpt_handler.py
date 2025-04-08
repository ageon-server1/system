from openai import OpenAI
from bot_config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

async def chat_reply(update, context):
    message = update.message.text
    chat = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}]
    )
    response = chat.choices[0].message.content
    await update.message.reply_text(response)
