import telebot
import time
import configparser

config = configparser.ConfigParser()
config.read('connect.ini')
config_data = config['DEFAULT']


bot = telebot.TeleBot("994681852:AAGdns6Oa4IWJvvC1x61HNERlzcjOoTNIdA")

# commands
@bot.message_handler(commands=['start', 'help'])
def handle_command_menu(message):
    bot.send_message(chat_id=message.chat.id,
                     text="✨hello")

# stickers
@bot.message_handler(content_types=["sticker"])
def echo_all(message):
    print("---------- @" + message.from_user.username, "aka ", message.from_user.first_name)
    print(message.json["sticker"]["thumb"]["file_unique_id"])

    if message.json["sticker"]["thumb"]["file_unique_id"] == "AQADY_pIDwAECUMAAg":
        bot.send_message(message.chat.id, "sticker with id: AQADY_pIDwAECUMAAg")

# text
@bot.message_handler(content_types=["text"])
def echo_all(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "добрый вечер")
    if message.text.lower() == "ж":
        bot.send_message(message.chat.id, "⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        bot.send_message(message.chat.id, "⬜️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️")
        bot.send_message(message.chat.id, "⬜️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️")
        bot.send_message(message.chat.id, "⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️")
        bot.send_message(message.chat.id, "⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️")
        bot.send_message(message.chat.id, "⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️")
        bot.send_message(message.chat.id, "⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️")
        bot.send_message(message.chat.id, "⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️")
        bot.send_message(message.chat.id, "⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️")
        bot.send_message(message.chat.id, "⬜️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️")
        bot.send_message(message.chat.id, "⬜️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️")
        bot.send_message(message.chat.id, "⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("Connection Error", e)
        time.sleep(15)
