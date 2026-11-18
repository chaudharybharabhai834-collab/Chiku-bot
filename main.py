from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "9102774911:AAFd-1m2F2ZoofH0RP6-zDPT-0kX5b3yZto"
ADMIN_ID = 9000201273
CHANNEL_1 = "@tumhara_channel_1"
CHANNEL_2 = "@tumhara_channel_2"
CHANNEL_1_LINK = "https://t.me/tumhara_channel_1"
CHANNEL_2_LINK = "https://t.me/tumhara_channel_2"
KEY = "CHIKU-1234"
SLOTS = 20
USED_SLOTS = 0

async def check_joined(bot, user_id):
    try:
        for ch in [CHANNEL_1, CHANNEL_2]:
            m = await bot.get_chat_member(ch, user_id)
            if m.status in ['left', 'kicked']:
                return False
        return True
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    left = SLOTS - USED_SLOTS
    keyboard = [
        [InlineKeyboardButton("🔥 GET KEY 🔥", callback_data="get_key")],
        [InlineKeyboardButton("CHENAL 1 💀", url=CHANNEL_1_LINK),
         InlineKeyboardButton("CHENAL 2 💀", url=CHANNEL_2_LINK)],
        [InlineKeyboardButton("Check Joined ✅", callback_data="check")],
    ]
    await update.message.reply_text(f"Join All Channels To Unlock 👇\n\n🔥 Slots Left: {left}/{SLOTS}", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global USED_SLOTS
    q = update.callback_query
    await q.answer()
    user_id = q.from_user.id
    if q.data in ["get_key", "check"]:
        joined = await check_joined(context.bot, user_id)
        if not joined:
            await q.message.reply_text("Pehle dono channel join karo fir Check Joined dabao!")
            return
        if USED_SLOTS >= SLOTS:
            await q.message.reply_text("Slots Full ho gaye! Kal try karo.")
            return
        USED_SLOTS += 1
        await q.message.reply_text(f"🔥 Tumhari KEY: {KEY}\nSlots Left: {SLOTS - USED_SLOTS}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
print("Bot Chal Gaya...")
app.run_polling()
