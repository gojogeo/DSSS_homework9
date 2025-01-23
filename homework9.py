from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler,  ContextTypes, filters

BOT_TOKEN = '7767512640:AAE9TEauZnBqTJV1LYHrzAN4b4ko4LuCpyE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, welcome to DSSS Homework 9:")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()