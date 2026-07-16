from telegram.ext import Application, CommandHandler, MessageHandler, filters
from brain import alphapilot_response
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text(
        "🚀 AlphaPilot X is online 🧠"
    )

async def chat(update, context):
    user_text = update.message.text
    response = alphapilot_response(user_text)
    await update.message.reply_text(response)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    print("🤖 AlphaPilot Telegram Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
