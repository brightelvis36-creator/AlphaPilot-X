from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from brain import alphapilot_response

TOKEN = "8994854153:AAEwFC_bEAk-yZR30vQdGytCrOtff80iAaM"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 AlphaPilot is online!\n\nYour AI assistant is ready."
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = alphapilot_response(user_message)

    await update.message.reply_text(reply)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    print("🚀 AlphaPilot Telegram Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()
