import telebot

mySlaveToken = '877949812:AAF1memBG6qplUprQZ3nmGORHtYWIdWQ7oQ'


def notification(masage):
    bot = telebot.TeleBot(mySlaveToken)
    bot.send_message(518356070, masage)


if __name__ == '__main__':
    notification('hello')