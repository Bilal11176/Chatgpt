import telebot
import openai

BOT_TOKEN = "84"
OPENAI_API_KEY = "sk"

openai.api_key = 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
bot = telebot.TeleBot(8493964723:AAFEO8FNAymNhgeJMSyjL_-jushXKv0H8yI)

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
