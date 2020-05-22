import telebot
import Config
import pyowm

from telebot import types

bot = telebot.TeleBot(Config.TOKEN)
# Начало работы команды "/start",и вопрос о городе.
city ='';
@bot.message_handler(commands=['start'])
def welcome(message):    # в функціЇ welcom буде храниться мысто яке вын веде,але прогорни на 33 строку і там побачиш щоб правильно написати треба використати +та змінна в якій записане місто,а так як я неможу записати цю змінну бо вона є функцією.
    sti = open('static/Botpogoda.png','rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,"Даров,я тестовый бот который  дает сведение о погоде в той или иной точке мира\n Введи название города.")

    @bot.message_handler(content_types=['text'])
    def welcome(message):






        def prox():
            owm = pyowm.OWM('f4640c34aeefad5699689b2a83c23678')
            observation = owm.weather_at_place(welcome)
            w = observation.get_weather()
            temperature = w.get_temperature('celsius')['temp']

@bot.message_handler(content_types=['text'])
def end(message):
    bot.send_message(message.from_user.id, "В городе"+welcome)#
















bot.polling(none_stop=True)




