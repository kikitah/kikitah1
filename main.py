import json
import requests
import telebot
from telebot import types
bot = telebot.TeleBot('6958850180:AAH5kp4B7MWK77QxAHAe95O8z8Sb1ChgcBc')
API = '34bce330409a326a70b4caea9ca605b4'
PROXY_URL ="http://proxy.server:3128"
@bot.message_handler(commands=['start'])
def start(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     item1 = types.KeyboardButton('Васюринская')
     item2 = types.KeyboardButton('Краснодар')
     item3 = types.KeyboardButton('Динская')
     markup.add(item1, item2, item3)
     bot.send_message(message.chat.id, 'Привет, {0.first_name}!' .format(message.from_user), reply_markup = markup)



@bot.message_handler(content_types=['text'] )
def get_weather(message):
    city = message.text.strip().lower()
    rec = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={API}&units=metric')
    if rec.status_code ==200:
        data = json.loads(rec.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас Погода:  {temp} °C\n')
        wind_speed = data['wind']['speed']
        if wind_speed < 5:
            bot.reply_to(message, 'Погода хорошая, ветра почти нет!')
        elif wind_speed < 10:
            bot.reply_to(message, 'На улице ветрено, оденьтесь чуть теплее!')
        elif wind_speed < 20:
            bot.reply_to(message, 'Ветер очень сильный, будьте осторожны, выходя из дома!')
        else:
            bot.reply_to(message, 'На улице шторм, на улицу лучше не выходить!')
    else:
        bot.reply_to(message, f'Город указан не верно!')

bot.polling(none_stop=True)