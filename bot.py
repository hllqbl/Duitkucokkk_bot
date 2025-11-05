from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

saldo = 0
transaksi = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('💵 **BOT KEUANGAN PRIBADI**\n\n/masuk [jumlah] - Catat pemasukan\n/keluar [jumlah] - Catat pengeluaran\n/saldo - Cek saldo')

async def masuk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global saldo
    if context.args:
        jumlah = int(context.args[0])
        kategori = context.args[1] if len(context.args) > 1 else "lainnya"
        
        saldo += jumlah
        transaksi.append(f"➕ Rp {jumlah} ({kategori})")
        
        await update.message.reply_text(f'✅ **Pemasukan Tercatat!**\n💰 Rp {jumlah:,}\n📁 {kategori}\n\n💳 Saldo: Rp {saldo:,}')

async def keluar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global saldo
    if context.args:
        jumlah = int(context.args[0])
        kategori = context.args[1] if len(context.args) > 1 else "lainnya"
        
        saldo -= jumlah
        transaksi.append(f"➖ Rp {jumlah} ({kategori})")
        
        await update.message.reply_text(f'✅ **Pengeluaran Tercatat!**\n💰 Rp {jumlah:,}\n📁 {kategori}\n\n💳 Saldo: Rp {saldo:,}')

async def cek_saldo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'💳 **Saldo Saat Ini:** Rp {saldo:,}')

def main():
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("masuk", masuk))
    app.add_handler(CommandHandler("keluar", keluar))
    app.add_handler(CommandHandler("saldo", cek_saldo))
    
    print("Bot sedang berjalan...")
    app.run_polling()

if __name__ == '__main__':
    main()
