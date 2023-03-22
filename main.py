import telebot
import json
import requests

bot=telebot.TeleBot("6187881425:AAFP3k8vpT20_24DeCxKiMO6EVaO6Iawmc4")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

def handle_prints(message):
    message = str(message)
    for i in message:
        if i == ",":
            print()
        print(i, end="")


@bot.message_handler(commands=['error'])
def send_error(message):
    handle_prints(message)
    bot.send_message(chat_id=message.chat.id,text="hey broo thanks")


@bot.message_handler(commands=['error'])
def send_error(message):
    handle_prints(message)
    bot.send_message(chat_id=message.chat.id,text="hey broo thanks")

@bot.message_handler(commands=['search'])
def send_error(message):
    handle_prints(message)
    print(type(message.id.text))
  #  mov_name=message.chat.text
   # print(mov_name)
    bot.send_message(chat_id=message.chat.id,text="this function works")




bot.infinity_polling()
