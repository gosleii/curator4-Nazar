import telebot

bot = telebot.TeleBot('6386618696:AAEnLOKlfoMwmv0ui7F3C2vaNZWBCEGbefs')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'это начало!!!', parse_mode='Markdown')

@bot.message_handler(commands=['jump'])
def main(message):
    bot.send_message(message.chat.id, 'ПРЫГААЙ!!! \nПРЫГААЙ!!!!!', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, '[ССЫЛОЧКА](https://vk.com/nazarius_big)', parse_mode='Markdown')


bot.infinity_polling()