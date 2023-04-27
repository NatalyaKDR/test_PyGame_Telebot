import pygame
import sys
from telebot import TeleBot

token='6106069845:AAGgLEXuUukU4QsWEpnrwyPQ02RkO8yQAn8'
bot= TeleBot(token)

@bot.message_handler()
def start(message):
    if message.text=='Привет' or message.text=='привет':
        bot.send_message(message.chat.id, "И тебе привет!")
    elif message.text=="Где кубик, Лебовски?":
        f = open('coord.txt', 'r')
        coor=f.read()
        bot.send_message(message.chat.id, coor)
        f.close()


bot.polling(none_stop=True)



