from random import randint, shuffle, sample
import telebot
from telebot.types import Message

bot = telebot.TeleBot('7320418747:AAGIcxzpciEMmMB9guari8-FxqLZulEk_Jk')
number = None



questions=[
        {"канберра":"Столица Австралии"},
        {"гренландия":"самый большой остров в мире?"},
        {"1c":"худший язык программирования?"},
        {"каспийское":"самое большое озеро в мире?"},
        {"эльбрус":"самая высокая гора в европе?"}
    ]

answers = [
    ['мельбрун',"сидней","канберра"],
    ["гренландия","крит","куриллы","окинава","гавайи"],
    ["php","c++","nodejs","python","javascript","1c"],
    ["байкал","каспийское","шира","мичиган","виктория"],
    ["эльбрус","монблан","альпы","джамалунгма","Шхара"]
]


# @bot.message_handler(commands=['start'])
# def start_bot(message:Message):
#     global number
#
#     bot.send_message(message.from_user.id,
#                      f'darova go poigraem v bolshe-menshe.\n im zaggadal number ot 0 do 100 make ugadai'
#                      )
#     number = randint(0,100)
a = answers.copy()
print(shuffle(a))

current_question=0
money=150

@bot.message_handler()
def process_message(message:Message):
    global current_question, money
    answerCopy = answers[current_question].copy()
    shuffle(answerCopy)
    bot.send_message(message.from_user.id, f"zdarova now we will play the game ugadaika")

@bot.message_handler()
def proces_message(message:Message):
    global current_question, money
    text = message.text.lower()
    for i in questions:
        print(i.keys())
        if i == text:
            money += 25
            bot.send_message(message.from_user.id, "you answer right molodec")

        else:
            money -= 25
            bot.send_message(message.from_user.id, "mdaaaaa.....")

    bot.send_message(message.from_user.id, f"your end winning: {money}")

bot.polling(none_stop=True, interval=0)







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    text = message.text.lower()
#     if text.isnumeric():
#         if int(text)> number:
#             bot.send_message(message.from_user.id,'your number is biggest')
#         elif int(text)<number:
#             bot.send_message(message.from_user.id, 'your number is lowest')
#         else:
#             bot.send_message(message.from_user.id, 'your got damn right')
#
#     else:
#         bot.send_message(message.from_user.id, 'You are a nonentity FUCK write numbers')
#
#
#
# bot.polling(none_stop=True, interval=0)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #