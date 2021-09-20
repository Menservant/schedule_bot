import random
import telebot
from telebot import types
import time
import datetime
import requests
import bs4

bot = telebot.TeleBot("1858364696:AAEIG72hGZSbdTacaO1XVq-GBKm6NTFcw6Q")
today = datetime.date.today()
hours = time.strftime("%H", time.localtime())
members = ("Александров", "Бубнов", "Воронин", "Каракулов", "Кучерина", "Мартынов", "Мелочников", "Михайлин", "Новикова"
           , "Санталин", "Серов", "Стрелков", "Тажетдинов", "Филатов", "Шатохин", "Щуркин", "Юдин")


@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_number = types.KeyboardButton("Кого сегодня нет?")
    how_are_you = types.KeyboardButton("Как делишки?")
    timetable = types.KeyboardButton("Расписание дай ботяра")
    keyboard.add(how_are_you, random_number, timetable)
    bot.send_message(message.chat.id,
                     "Здарова {} я учусь выдавать расписание"
                     .format(message.from_user.first_name), parse_mode="html", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def talk(message):
    if message.chat.type == "private":
        if message.text == "Кого сегодня нет?":
            bot.send_message(message.chat.id, f"Сегодня нет : {random.choice(members)}")
        elif message.text == "Как делишки?":
            bot.send_message(message.chat.id, "Всё чики-брики, только разработчик даун")
        elif message.text == "Расписание дай ботяра" and today.weekday() != 4 and today.weekday() != 5:
            bot.send_message(message.chat.id, "Завтра на блядскую учёбу")
        else:
            bot.send_message(message.chat.id, "{} чё пристал, не знаю я что ответить.".format(message.from_user.first_name))


bot.polling()
