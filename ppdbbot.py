import telebot

api = '1670719772:AAGS7oG-JFzp_HVvHNF1j-s9mpzdIssrD4w'
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hallo Apa Kabar??')


@bot.message_handler(commands=['Help'])
def send_welcome(message):
    bot.reply_to(message, 'Apa yang bisa saya bantu')

    print('bot start running')
    bot.polling()
