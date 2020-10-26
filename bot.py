import telebot
import time
import configparser

config = configparser.ConfigParser()
config.read('connect.ini')
config_data = config['DEFAULT']


bot = telebot.TeleBot("994681852:AAGdns6Oa4IWJvvC1x61HNERlzcjOoTNIdA")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Вопросы')



def handleAddAnswer(answer, chatId):
    data['messages'].append("# " + answer)
    dataFile = open('storage.json', 'w', encoding="utf-8")
    json.dump(data, dataFile, ensure_ascii=True)
    dataFile.close()
    bot.send_message(chatId, text = "Ваш ответ успешно обработан")

def handleSearch(query, chatID):
    if(len(data['messages']) == 0):
        return
    best_match_answer = get_best_match(query, )
    bot.send_message(chatID, text = best_match_answer, parse_mode='Markdown')

def isNumericString(strNum):
    try:
        int(strNum)
    except:
        return False
    return True

def handleQuestionHeaders(chatId):
    headers = ''
    i = 0
    for question in data['messages']:
        i += 1
        header = ''
        header_started = False
        for char in question:
            if header_started:
                header += char
            if char == '#':
                header_started = True
            if char == '\n' and header != '':
                header_started = False
                headers += '\n' + str(i) + header
                header = ''
    bot.send_message(chatId, text = headers)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text="Добро пожаловать", reply_markup=keyboard1)
=======
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('1', '2', '3')
keyboard2.row('4', '5', '6')
keyboard2.row('7', '8', '9')
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
                          "1.фундаментальна система розв'язків\n"
                          "2.ранг оператора\n"
                          "3.арифметичний n-вимірний простір\n"
                          "4.лінійний оператор\n"
                          "5.однорідна система лінійних рівнянь\n"
                          "6.система лінійних рівнянь\n"
                          "7.лінійні та векторні простори\n"
                          "8.n-вимірний вектор\n"
                          "9.ядро оператора(позначення, розмірність)\n", reply_markup=keyboard2)
    elif message.text == '1':
        bot.send_message(message.chat.id, text="Фундаментальною системою розв'язків системи неоднорідних рівнянь називається така лінійно незалежна сукупність її розв'язків, що всякий розв'язок даної системи є якоюсь лінійною комбінацією розв'язків цієї сукупності")
    elif message.text == '2':
        bot.send_message(message.chat.id, text="Розмірність області значень LnA називають рангом оператора А і позначають rang A(приметка: тут л н,а не логарифм)\n")
    elif message.text == '3':
        bot.send_message(message.chat.id, text="Арифметичним n-вимірним простором будемо називати множину усіх n-вимірних векторів, на якій визначено операції додавання векторів та множення векторів")
    elif message.text == '4':
        bot.send_message(message.chat.id, text="Оператор у векторному просторі L - функція множиною визначення і множиною значень якої є простір L\n"
                                                "Критерії лінійності:\n"
                                                "1) якщо аргумент помножити на число, то і результат множиться це число, тобто числовий множник аргументу можна винести за знак операції:\n"
                                                "f (\ alpha x) = \ alpha f (x)\n"
                                                "2) якщо аргумент замінити сумою двох доданків, то результат буде дорівнює сумі результатів для кожного доданка:\n"
                                                "f(x_1 + x_2) = f (x_1) + f (x_2))")
    elif message.text == '5':
        bot.send_message(message.chat.id, text="Система лінійних рівнянь називається однорідною (СЛОР), якщо вільний член у кожному рівнянні дорівнює нулю")
    elif message.text == '6':
        bot.send_message(message.chat.id, text="Рівняння з n невідомими х1,х2,…,хn називається лінійним, якщо його можна подати у вигляді:\n"
                          "а1х1+а2х2+…+ аnхn= b , (1.1)\n"
                          "де а1,а2,…,ап– коефіцієнти, b – вільний член рівняння (дійсні числа)")        
    elif message.text == '7':
        bot.send_message(message.chat.id, text="Множина V елементів x, y, z,… називається лінійним, або векторним простором, якщо сума х+у довільних двох її елементів х, у і добуток ?х кожного її елемента х на будь-яке число ? теж належать множині V")        
    elif message.text == '8':
        bot.send_message(message.chat.id, text="Будь-який вектор арифметичного простору будемо розуміти як упорядкувану н-ку дійсних чисел")        
    elif message.text == '9':
        bot.send_message(message.chat.id, text="Ядром лінійного оператора А простору Ln називається сукупність всіх векторів цього простору, які оператором А відображаються в нульовий вектор.\n"
                           "Ядро лінійного оператора позначається KerA.\n" 
                           "Розмірність ядра оператора А називається дефектом цього оператора\n")             
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, text=" Хорошо", reply_markup=keyboard1)

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
