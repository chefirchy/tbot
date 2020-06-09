import telebot
import time
import configparser

config = configparser.ConfigParser()
config.read('connect.ini')
config_data = config['DEFAULT']


bot = telebot.TeleBot("994681852:AAGdns6Oa4IWJvvC1x61HNERlzcjOoTNIdA")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Вопросы')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('1', '2', '3', '4', '5')
keyboard2.row('6', '7', '8', '9', '10')
keyboard2.row('11', '12', '13', '14', '15')
keyboard2.row('16', '17', '18', '19', '20')
keyboard2.row('21', '22', '23', '24', '25')
keyboard2.row('Назад')
@bot.message_handler(commands=['Назад'])
def back(message):
    bot.send_message(message.chat.id, 'Отлично', reply_markup=keyboard1)

# commands
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text="Добро пожаловать", reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == 'Вопросы':
        bot.send_message(message.chat.id, text="Список вопросов:\n"
                          "1.Виберіть рядок, у якому всі словосполуки перекладені правильно\n"
                          "2.Виберіть рядок, який містить правильний переклад речення <<директор находится в командировке в киевском университете, который находится на улице...\n"
                          "3.Виберіть рядок, у якому правильно перераховані види перекладу\n"
                          "4.Позначте рядок, у якому всі терміни утворено способом вторичної номінації\n"
                          "5.Позначте рядок, у якому всі терміни невідмінювані іменники в укр. мові\n"
                          "6.Позначте рядок, у якому терміносполуки потребують редагування\n"
                          "7.Загальнонаукові терміни подано у рядку\n"
                          "8.позначте рядок, у якому правильно дібрано українські відповідники до іншомовних термінів\n"
                          "9.Позначте рядок, у якому всі терміни належать до однієї терміносистеми", reply_markup=keyboard2)
    elif message.text == '1':
        bot.send_message(message.chat.id, text="Зазвичай, внаслідок, з одного боку, під час аналізу, у жодному разі")
    elif message.text == '2':
        bot.send_message(message.chat.id, text="Директор перебуває у відрядженні в києвському університеті, який розташовується на вулиці довженка\n")
    elif message.text == '3':
        bot.send_message(message.chat.id, text="Дослівний, адекватний, точний, реферативний, вільний, буквальний, анотаційний\n")
    elif message.text == '4':
        bot.send_message(message.chat.id, text="чиста конкуренція, сатиновий друк, споживчий кошик, водяний знак\n")
    elif message.text == '5':
        bot.send_message(message.chat.id, text="Сопрано,піанісимо, СЕЗ, сальто, апріорі, реле, вето, адажіо")
    elif message.text == '6':
        bot.send_message(message.chat.id, text="Науковий тезис, емоціональне тло, стержень економічної політики, ліквідовні кошти, алгебраїчний вираз, кромваотний валютний курс")        
    elif message.text == '7':
        bot.send_message(message.chat.id, text="Гіпотеза, закон, концепція, теорія, синтез, аргумент, класифікація, варіант, категорія, функція")        
    elif message.text == '8':
        bot.send_message(message.chat.id, text="Нарративний - розповідний, латентний - прихований.......\n""ексклюзивний - винятковий, варіабельний - змінний")        
    elif message.text == '9':
        bot.send_message(message.chat.id, text="Шхуна, док, шкіпер, мічман, кіль")             
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, text=" Хорошо", reply_markup=keyboard1)
        
        
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
