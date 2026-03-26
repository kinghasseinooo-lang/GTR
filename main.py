import telebot
from telebot import types

# ضع توكن البوت الأساسي (المصنع) هنا
API_TOKEN = '8523010431:AAGmfBuU0zgRv9fQdQ8tlN8zqsWRABnpcds'
# ضع يوزر قناتك للاشتراك الإجباري (@SSWE7)
CHANNEL_USERNAME = 'متحركات GIF'
# ايدي المطور (حتى توصلك رسائل التواصل)
ADMIN_ID = 7481039233  # غيره لايديك (ID الخاص بك)

bot = telebot.TeleBot(API_TOKEN)

# دالة التحقق من الاشتراك الإجباري
def check_subscription(user_id):
    try:
        status = bot.get_chat_member(f"@{CHANNEL_USERNAME}", user_id).status
        if status in ['member', 'administrator', 'creator']:
            return True
        return False
    except:
        return False

@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    
    # التحقق من الاشتراك
    if not check_subscription(user_id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("اشترك بالقناة أولاً 📢", url=f"https://t.me/{CHANNEL_USERNAME}")
        markup.add(btn)
        bot.send_message(message.chat.id, f"هلاً بيك عيوني.. لازم تشترك بقناتنا حتى تكدر تستخدم المصنع وتصنع بوتك ⚠️\n\nاشترك هنا: @{CHANNEL_USERNAME}\nوبعدين ارسل /start", reply_markup=markup)
        return

    # قائمة الأزرار الرئيسية
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("صناعة بوت جديد 🛠")
    item2 = types.KeyboardButton("تواصل مع المطور 💬")
    item3 = types.KeyboardButton("شلون أستخدم المصنع؟ ❓")
    markup.add(item1, item2)
    markup.add(item3)
    
    bot.send_message(message.chat.id, "هلاً بيك بمصنع البوتات الخاص بيك 🏠\nمنورنا يا ورد.. اختار من الأزرار الجوة شتريد تسوي؟", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "صناعة بوت جديد 🛠":
        bot.send_message(message.chat.id, "خوش، دزلي 'التوكن' مال بوتك اللي جبته من @BotFather\nواني راح أفعله الك فوراً.")
    
    elif message.text == "تواصل مع المطور 💬":
        bot.send_message(message.chat.id, "اكتب رسالتك وراح توصل للمطور مباشرة..")
        bot.register_next_step_handler(message, send_to_admin)

    elif message.text == "شلون أستخدم المصنع؟ ❓":
        bot.send_message(message.chat.id, "1. تروح لبوت فاذر @BotFather وتصنع بوت.\n2. تنسخ التوكن (Token).\n3. ترجع هنا وتدزه للمصنع.\nوبس، بوتك يصير جاهز!")

# دالة التواصل
def send_to_admin(message):
    # إرسال الرسالة للأدمن
    bot.send_message(ADMIN_ID, f"وصلتك رسالة تواصل جديدة 📩\nمن: {message.from_user.first_name}\nاليوزر: @{message.from_user.username}\nالرسالة: {message.text}")
    # تأكيد للمستخدم
    bot.send_message(message.chat.id, "رسالتك وصلت للمطور، راح نجاوبك بأقرب وقت.")

print("المصنع شغال..")
bot.polling()
