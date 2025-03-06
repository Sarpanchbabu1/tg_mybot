import os
import re
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackContext

# Load bot token from environment variables
BOT_TOKEN = os.getenv("7876959388:AAGPi3CaF_mqGlZJUOmrcvR--VT8NGBPzp0")

# Function to check if a message contains a link
def contains_link(text):
    link_pattern = r"(https?://\S+|www\.\S+)"
    return re.search(link_pattern, text)

# Function to handle messages and remove links
async def filter_links(update: Update, context: CallbackContext):
    if update.message and contains_link(update.message.text):
        await update.message.delete()
        await update.message.reply_text("No links allowed!", quote=True)

# Start command handler
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am a protection bot. I will remove links from messages.")

# Main function to start the bot
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_links))

    # Start the bot
    await app.run_polling()

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
