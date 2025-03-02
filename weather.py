import telebot


bot = telebot.TeleBot('1974247687:AAGe4o8naTcpLA2sTg5eL-GJVAyy54gTwlA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Please enter city:")
    
    
@bot.message_handler(content_type=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    bot.send_message(message.chat.id, f"Your city is: {city}")
    
bot.polling(none_stop=True)