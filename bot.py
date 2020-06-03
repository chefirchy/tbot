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
@bot.message_handler(commands=['j', 'J'])
def handle_command_menu(message):
    bot.send_message(chat_id=message.chat.id,
                     text="⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n"
                          "⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬛️⬜️\n"
                          "⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬛️⬜️\n"
                          "⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️\n"
                          "⬜️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬜️\n"
                          "⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️\n"
                          "⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬛️⬜️\n"
                          "⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬛️⬜️\n"
                          "⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n")
@bot.message_handler(commands=['Oof', 'oof'])
def handle_command_menu(message):
    bot.send_message(chat_id=message.chat.id,
                     text="🟨🟨🟨🟨🟨🟨\n"
                           "🟨⬜️⬜️🟨⬜️⬜️🟨\n"
                           "🟨⬜️⬛️🟨⬛️⬜️🟨\n"
                           "🟨🟨🟨🟨🟨🟨🟨\n"
                           "🟨🟥⬜️🟥⬜️🟥🟥🟨\n"
                           "🟨🟥🟥🟥🟥🟥🟨🟨\n"
                           "🟨⬜️🟥⬜️🟥⬜️🟨🟨\n"
                           "🟨🟨🟨🟨🟨🟨🟨\n")
@bot.message_handler(commands=['a', 'A'])
def handle_command_menu(message):
    bot.send_message(chat_id=message.chat.id,
                     text="1.фундаментальна система розв'язків\n"
                          "2.ранг оператора\n"
                          "3.арифметичний n-вимірний простір\n"
                          "4.Оператор у векторному просторі\n")
@bot.message_handler(commands=['1', 'o'])
def handle_command_menu(message):
    bot.send_message(chat_id=message.chat.id,
                     text="Фундаментальною системою розв'язків системи неоднорідних рівнянь називається така лінійно незалежна сукупність її розв'язків, що всякий розв'язок даної системи є якоюсь лінійною комбінацією розв'язків цієї сукупності") 
@bot.message_handler(commands=['2', 'd'])
def handle_command_menu(message):
    bot.send_message(chat_id=message.chat.id,
                     text="Розмірність області значень LnA називають рангом оператора А і позначають rang A\n")
@bot.message_handler(commands=['3', 't'])
def handle_command_menu(message):
    bot.send_message(chat_id=message.chat.id,    
                     text="Арифметичним n-вимірним простором будемо називати множину усіх n-вимірних векторів, на якій визначено операції додавання векторів та множення векторів")
      
    

# stickers
@bot.message_handler(content_types=["sticker"])
def echo_all(message):
    print("---------- @" + message.from_user.username, "aka ", message.from_user.first_name)
    print(message.json["sticker"]["thumb"]["file_unique_id"])

    if message.json["sticker"]["thumb"]["file_unique_id"] == "AQADY_pIDwAECUMAAg":
        bot.send_message(message.chat.id, "sticker with id: AQADY_pIDwAECUMAAg")

# text





while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("Connection Error", e)
        time.sleep(15)
