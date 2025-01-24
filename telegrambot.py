
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler,  ContextTypes, filters
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model():
    model_name = "gpt2"
    #model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

# Perform inference
def generate_response(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=250, do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
    

model, tokenizer = load_model()

BOT_TOKEN = '7767512640:AAE9TEauZnBqTJV1LYHrzAN4b4ko4LuCpyE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, welcome to DSSS Homework 9:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input = update.message.text
    await update.message.reply_text("Processing your request...")
    response = generate_response(model, tokenizer, input)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()