import telebot
from telebot import types
import json
import another_one

jsonH = json.load(open('source/config.json'))

tokken = jsonH['tokken']

bot = telebot.TeleBot(tokken)




@bot.message_handler(commands=['fun'])
def start(message):
    mark= types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1= types.KeyboardButton("tell me a joke")
    btn2= types.KeyboardButton("what can i do?")
    mark.add(btn1,btn2)
    bot.send_message(message.chat.id, text="choose a button and click it ",reply_markup=mark)



@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "tell me a joke":
        reply = another_one.joke()
        bot.send_message(message.chat.id, text=reply)

    elif message.text == "what can i do?":
        reply = another_one.bored()
        bot.send_message(message.chat.id, text=reply)

    else:
        bot.send_message(message.chat.id, text=("this is not a command for start write /fun"))
        

bot.infinity_polling()





