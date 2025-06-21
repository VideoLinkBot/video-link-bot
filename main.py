import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import yt_dlp

BOT_TOKEN = "8066907048:AAEWVhSO979loFadCDaDRkPwnbSNK_kupEE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! YouTube link yuboring, men video yuklab beraman.")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Video yuklanmoqda...")

    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        await update.message.reply_video(video=open('video.mp4', 'rb'))
        os.remove('video.mp4')
    except Exception as e:
        await update.message.reply_text(f"Xatolik: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("video", download))
    app.run_polling()

if __name__ == '__main__':
    main()
