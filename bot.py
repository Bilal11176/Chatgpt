import telebot
import openai

BOT_TOKEN = "84"
OPENAI_API_KEY = "sk"

openai.api_key = OPENAI_API_KEY
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🤖 Welcome to AI Assistant Bot\n\n"
        "Ask me anything!\n"
        "⚠️ Educational purposes only"
    )

@bot.message_handler(func=lambda message: True)
def ai_reply(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "⚠️ AI is busy. Try again later.")

bot.polling()