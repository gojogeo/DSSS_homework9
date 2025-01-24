
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler,  ContextTypes, filters
from openai import OpenAI
import openai
import os

os.environ["OPENAI_API_KEY"] =  "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"
client = OpenAI()

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model = "gpt2",
        messages =[{"role":"user",  "content":[{"type":"text", "text":prompt}]}]
    )
    return response.choices[0].message.strip()


BOT_TOKEN = '7767512640:AAE9TEauZnBqTJV1LYHrzAN4b4ko4LuCpyE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, welcome to DSSS Homework 9:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input = update.message.text
    await update.message.reply_text("Processing your request...")
    response = chat_with_gpt(input)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()