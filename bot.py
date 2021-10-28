import os

import telebot
from flask import Flask, request

TOKEN = '2082512937:AAEDwkbIToD2v5bKpO9Muq1Vy4veql0LR90'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://guarded-reaches-07854.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

"""
@post('/')
def main():
    data = bottle_request.json  # <--- extract all request data
    print(data)

    return


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
"""

# https://guarded-reaches-07854.herokuapp.com
# api.telegram.org/bot2082512937:AAEDwkbIToD2v5bKpO9Muq1Vy4veql0LR90/setWebHook?url=https://guarded-reaches-07854.herokuapp.com/
# api.telegram.org/bot2082512937:AAEDwkbIToD2v5bKpO9Muq1Vy4veql0LR90/setWebHook?url=https://ce97-193-144-61-240.ngrok.io/
# api.telegram.org/bot2082512937:AAEDwkbIToD2v5bKpO9Muq1Vy4veql0LR90/getWebhookInfo
