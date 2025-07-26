from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from utils import load_config, is_official_account

config = load_config()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎉 欢迎使用 九色™️ 视频官方防伪验证机器人！\n\n"
        "如果有账号主动联系你，请务必提高警惕。你可以将对方的 @账号 输入到这里，我们会立即帮你验证该账号是否为九色™️官方认证账号。\n\n"
        "🛡 防诈骗，从验证开始。"
    )
    await update.message.reply_text(text)

async def list_accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    accounts = config["public_accounts"]
    msg = "📋 当前公开的官方账号如下：\n\n"
    for acc in accounts:
        msg += f"✅ {acc}\n"
    await update.message.reply_text(msg)

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        reported = context.args[0]
        await update.message.reply_text(f"✅ 已记录举报：{reported}\n我们建议您立即阻止并避免与其互动。")
    else:
        await update.message.reply_text("请使用格式：/report @账号")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    if not query.startswith("@"):
        await update.message.reply_text("⚠️ 请输入 @ 开头的 Telegram 用户名，例如：@JiuSeBot")
        return
    if is_official_account(query):
        await update.message.reply_text(f"✅ {query} 是我们认证的官方账号。")
    else:
        await update.message.reply_text(f"❌ {query} 并非我们的官方账号，可能为冒充，请勿轻信。")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("list", list_accounts))
app.add_handler(CommandHandler("report", report))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.run_polling()