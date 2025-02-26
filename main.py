import telebot
import webbrowser
from telebot import types

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
    
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    temp = types.InlineKeyboardMarkup()
    temp.add(types.InlineKeyboardButton("open page", url="https://google.com"))
    temp.add(types.InlineKeyboardButton("Delete", callback_data='delete'))
    temp.add(types.InlineKeyboardButton("Update", callback_data='edit'))
    
    bot.reply_to(message, 'Good!', reply_markup=temp)
    
    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    
    elif callback.data == 'edit':
        bot.edit_message_text("edit text", callback.message.chat.id, callback.message.message_id)
    
    
bot.polling(none_stop=True)