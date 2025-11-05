import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Ganti dengan token bot Anda
TOKEN = os.getenv('TELEGRAM_TOKEN', 'YOUR_BOT_TOKEN_HERE')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Halo! Bot sedang berjalan dengan baik.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
    Bot Commands:
    /start - Memulai bot
    /help - Menampilkan bantuan
    """
    await update.message.reply_text(help_text)

async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f'Anda mengatakan: {text}')

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

def main():
    try:
        print("Memulai bot...")
        
        # Build application
        app = Application.builder().token(TOKEN).build()
        
        # Add handlers
        app.add_handler(CommandHandler("start", start_command))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
        
        # Error handler
        app.add_error_handler(error_handler)
        
        print("Bot berhasil diinisialisasi. Menjalankan polling...")
        
        # Start polling
        app.run_polling(
            allowed_updates=Update.ALL_TYPES,
            drop_pending_updates=True
        )
        
    except Exception as e:
        print(f"Error saat menjalankan bot: {e}")

if __name__ == "__main__":
    main()
