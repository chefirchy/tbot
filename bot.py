import telebot
import json
import time
import configparser
from search_engine import get_best_match

config = configparser.ConfigParser()
config.read('connect.ini')
config_data = config['DEFAULT']

dataFile = open('storage.json', encoding='utf-8')
data = json.load(dataFile)
dataFile.close()



keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Вопросы','Помощь')

def handleAddAnswer(answer, chatId):
    data['messages'].append("# " + answer)
    dataFile = open('storage.json', 'w', encoding="utf-8")
    json.dump(data, dataFile, ensure_ascii=True)
    dataFile.close()
    bot.send_message(chatId, text = "Ваш ответ успешно обработан")

def handleSearch(query, chatID):
    if(len(data['messages']) == 0):
        return
    best_match_answer = get_best_match(query, data['messages'])
    if (best_match_answer == '' or best_match_answer == None):
        return
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
@bot.message_handler(commands=['Назад'])
def back(message):
    bot.send_message(message.chat.id, 'Отлично', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == 'Помощь':
        bot.send_message(message.chat.id, text="Пример добавления вопроса:\n"
                         "Добавить ответ:Сюда пишем вопрос\n"
                         "Тут ответ\n")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    
        if message.text.lower().startswith('добавить ответ:'):
            if (message.from_user.id == 420851241):
                handleAddAnswer(message.text[15:], message.chat.id)
        elif (isNumericString(message.text) and int(message.text) <= len(data['messages'])):
            bot.send_message(message.chat.id, text=data['messages'][int(message.text) - 1])
        elif message.text.lower() == 'Вопросы':
            handleQuestionHeaders(message.chat.id)
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, text="Хорошо", reply_markup=keyboard1)
        else:
            handleSearch(message.text, message.chat.id)

        
@bot.message_handler(content_types=["sticker"])
def echo_all(message):
    print("---------- @" + message.from_user.username, "aka ", message.from_user.first_name)
    print(message.json["sticker"]["thumb"]["file_unique_id"])

    if message.json["sticker"]["thumb"]["file_unique_id"] == "AQADY_pIDwAECUMAAg":
        bot.send_message(message.chat.id, "sticker with id: AQADY_pIDwAECUMAAg")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("Connection Error", e)
        time.sleep(15)

