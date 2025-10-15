import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from google.generativeai import TextGenerationClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

client = TextGenerationClient(api_key=api_key)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text
    response = client.generate_text(
        model="gemini-1.5",
        prompt=user_input
    )
    update.message.reply_text(response.text)

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
print("MeyraPlantDoctorBot is running securely...")
updater.idle()
