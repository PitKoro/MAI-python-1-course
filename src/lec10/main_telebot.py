import os
# Импортируем библиотеку
import telebot
from telebot import types

# Кнопки в сообщении
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://yandex.ru/maps/213/moscow/?ll=37.632803%2C55.743607&mode=whatshere&whatshere%5Bpoint%5D=37.638243%2C55.743296&whatshere%5Bzoom%5D=14.32&z=14.32'))
    bot.send_message(message.chat.id, 'перейди по ссылке', reply_markup=markup)


#Указываем к какому боту мы будем обращаться.
# для этого указываем token нужного бота
bot = telebot.TeleBot('5858782359:AAHiXwtYNQPcoANrTPgOAeZCbz0slj6VHmE')

#отслеживание команд
@bot.message_handler(commands=['start', 'website'])
def start(message):
    #функция автоматически принимает один параметр - сообщение от пользователя
    #  Ответим пользователю сообщением
    if message.text == "/start":
        bot.send_message(message.chat.id, "<b>Привет от бота!</b>", parse_mode='html')
    elif message.text == "/website":
        website(message)




#отслеживание текста
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, "И тебе хай)")
    elif message.text == "фото":
        photo = open('img/eva.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "loc":
        bot.send_location(message.chat.id, 55.743296, 37.638243)
    elif message.text == "Сайт":
        website(message)
        

# отслеживание файлов
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Классно выглядишь!')
    


# Кнопки в сообщении
@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://yandex.ru/maps/213/moscow/?ll=37.632803%2C55.743607&mode=whatshere&whatshere%5Bpoint%5D=37.638243%2C55.743296&whatshere%5Bzoom%5D=14.32&z=14.32'))
    bot.send_message(message.chat.id, 'перейди по ссылке', reply_markup=markup)

#запускаем бота
bot.polling(non_stop=True)