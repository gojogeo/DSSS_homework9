
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler,  ContextTypes, filters
import requests

LLM_BASE_URL = "http://127.0.0.1:1234"


BOT_TOKEN = '7767512640:AAE9TEauZnBqTJV1LYHrzAN4b4ko4LuCpyE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, welcome to DSSS Homework 9:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input = update.message.text
    await update.message.reply_text("Processing your request...")
    payload = {
    "model": "llama-3.2-1b-instruct",  
    "prompt": input,
    "max_tokens": 100,
    "temperature": 0.7
    }
    response = requests.post(f"{LLM_BASE_URL}/v1/completions", json=payload)
    data = response.json()
    output = data.get("choices", [{}])[0].get("text", "No response")
    
    await update.message.reply_text(output)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()