import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from utils import load_config, is_official_account

BOT_TOKEN = os.environ["BOT_TOKEN"]
config = load_config()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 欢迎使用 九色™️ 视频官方防伪验证机器人！\n输入 @账号 验证是否为官方账号。"
    )

async def list_accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    accounts = config["public_accounts"]
    text = "📋 当前公开的官方账号：\n" + "\n".join(f"✅ {a}" for a in accounts)
    await update.message.reply_text(text)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    if is_official_account(query):
        await update.message.reply_text(f"✅ {query} 是官方账号。")
    else:
        await update.message.reply_text(f"❌ {query} 并非官方账号。")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN)
    application = app.build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("list", list_accounts))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    application.run_polling()

if __name__ == "__main__":
    main()
