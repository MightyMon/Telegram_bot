import telebot
import json
import requests

bot=telebot.TeleBot("<bot-token>")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey there how are you doing? \n For more information and to know commands available go to /help")

@bot.message_handler(commands=['help'])
def send_menu(message):
    bot.reply_to(message, "use the /search command preceeding with the movie name to get the information abot the movie")

@bot.message_handler(commands=['search'])
def send_data(message):
    
    
    mov_name=message.text
    mov_name="http://www.omdbapi.com/?<apikey>"+mov_name[7:]
    response = requests.get(mov_name)
    data=response.json()
    img_url=data['Poster']
    image_caption="Title:  "+data['Title']+"\n"+"\n"+'Date released:  '+data['Released']
  

    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption=image_caption)




bot.infinity_polling()
