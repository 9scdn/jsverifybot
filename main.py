import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)
from utils import load_config, is_official_account

BOT_TOKEN = os.environ["BOT_TOKEN"]
config = load_config()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 欢迎使用 九色™️ 视频官方防伪验证机器人！\n\n"
        "输入对方的 @账号，即可验证是否为官方账号。"
    )

async def list_accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    accounts = config["public_accounts"]
    text = "📋 当前公开的官方账号如下：\n" + "\n".join(f"✅ {acc}" for acc in accounts)
    await update.message.reply_text(text)

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(f"✅ 已记录举报：{context.args[0]}")
    else:
        await update.message.reply_text("⚠️ 格式：/report @账号")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    if not query.startswith("@"):
        await update.message.reply_text("⚠️ 请输入 @开头的账号，例如 @JiuSeBot")
        return
    if is_official_account(query):
        await update.message.reply_text(f"✅ {query} 是我们认证的官方账号")
    else:
        await update.message.reply_text(f"❌ {query} 不是官方账号，请谨慎！")


async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("list", list_accounts))
    app.add_handler(CommandHandler("report", report))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
