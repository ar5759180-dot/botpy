from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8677313490:AAHhKeLWRoWPehPMzQ8Ocm35GrFzC3e8pfI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات من خوش اومدی 👋")

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "سلام" in text:
        await update.message.reply_text("سلام 😊")

    else:
        await update.message.reply_text("پیامت را دریافت کردم.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

print("ربات فعال شد...")

app.run_polling()
