import telebot

mySlaveToken = 'Your bot token here'


def notification(masage):
    bot = telebot.TeleBot(mySlaveToken)
    bot.send_message(518356070, masage)


if __name__ == '__main__':
    notification('hello')
