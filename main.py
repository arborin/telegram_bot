import telebot
import webbrowser

bot = telebot.TeleBot('1974247687:AAGe4o8naTcpLA2sTg5eL-GJVAyy54gTwlA')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, '<b>H</b>ello!', parse_mode='html')
    
    
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, message)
    
@bot.message_handler(commands=['browser'])
def browser(message):
    webbrowser.open('https://google.com')
    
bot.polling(none_stop=True)