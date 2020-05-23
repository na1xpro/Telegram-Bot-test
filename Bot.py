import telebot
import Config
import pyowm

from telebot import types

bot = telebot.TeleBot(Config.TOKEN)
owm = pyowm.OWM('f4640c34aeefad5699689b2a83c23678')
@bot.message_handler(commands=['start'])
def handle_text (message):
    bot.send_message(message.chat.id, "Введите город")
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        txt = message.text
        observation = owm.weather_at_place(txt)
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')['temp']
        bot.send_message(message.chat.id, 'В городе ' +txt + ":" ' сейчас ' +str(temperature) +" по по цельсию")


















bot.polling(none_stop=True)




