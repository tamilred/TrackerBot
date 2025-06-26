from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "@your_channel_here"

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.chat_member.new_chat_member
    if member.status == "member":
        user = member.user
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"🎉 New member joined: {user.full_name} (ID: {user.id})"
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    handler = ChatMemberHandler(new_member, ChatMemberHandler.CHAT_MEMBER)
    app.add_handler(handler)
    print("Bot is running...")
    app.run_polling()
