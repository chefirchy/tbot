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
                          "9.Позначте рядок, у якому всі терміни належать до однієї терміносистеми\n", 
                          "10.Стандартизація термінології – це\n"
                          "11.Терміносистема - це\n"
                          "12.Термін - це\n"
                          "13.Друкована стандартна форма документа з реквізитами, що містять постійну інформацію, має назву\n"
                          "14.Копія офіційного документа, що відтворює певну його частину й відповідно засвідчена, має назву\n"
                          "15.Публічне монологічне мовлення\n"
                          "16.Виберіть рядок, у якому всі етикетні формули можуть вживатися в науковому мовленні\n"
                          "17.Виберіть рядок, у якому правильно визначена структура наукового тексту\n"
                          "18.Виберіть рядок, у якому правильно складено бібліографічний опис джерела (згідно стандарту ДСТУ 8302:2015 «Інформація та документація. Бібліографічне посилання. Загальні положення та правила складання»\n"
                          "19.Усвідомити прочитане і стисло відтворити в пам’яті зміст наукового джерела допомагає…\n"
                          "20.Виберіть рядок з правильно сформульованим реченням наукового стилю\n"
                          "21.Виберіть рядок, у якому правильно перераховані різновиди конспектів:\n"
                          "22-26 задания на соответствие\n"
                          "22.Установіть відповідність між визначеннями понять та термінами на їх позначення\n"
                          "23.Установіть відповідність між визначеннями перекладу та його різновидом:\n"
                          "24.Установіть відповідність між варіантами слів і їх видами\n"
                          "25.Установіть відповідність між варіантами слів і їх видами номер 2\n"
                          "26.нема",reply_markup=keyboard2)
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
    elif message.text == '10':
        bot.send_message(message.chat.id, text="Вироблення термінів-еталонів, унормування термінів в межах однієї країни або в межах групи країн")
    elif message.text == '11':
        bot.send_message(message.chat.id, text="сукупність термінів, що обусловлює певну галузь науки чи техніки")    
    elif message.text == '12':
        bot.send_message(message.chat.id, text="Позначення певного поняття у фаховій мові за допомогою лінгвістичного виразу")    
    elif message.text == '13':
        bot.send_message(message.chat.id, text="бланк")    
    elif message.text == '14':
        bot.send_message(message.chat.id, text="витяг")    
    elif message.text == '15':
        bot.send_message(message.chat.id, text="Риторики")    
    elif message.text == '16':
        bot.send_message(message.chat.id, text="Справедливо наголошував, дякую за зауваження, передусім зазначимо")    
    elif message.text == '17':
        bot.send_message(message.chat.id, text="Вступна, дослідна, висновкова частина") 
    elif message.text == '18':
        bot.send_message(message.chat.id, text="Співаковський О.В., Львов М.С., Кравцов Г.М. Інноваційні методи управління інформаційними активами вищого навчального закладу Компютер у школі та сімї. Випуск 3.Київ, 2013. С. 3-7.")
    elif message.text == '19':
        bot.send_message(message.chat.id, text="План")
    elif message.text == '20':
        bot.send_message(message.chat.id, text="Ця стаття потребує перевірки експериментальної частини")
    elif message.text == '21':
        bot.send_message(message.chat.id, text="Плановий, вільний, опорний, тематичний, текстуальний")
    elif message.text == '22':
        bot.send_message(message.chat.id, text="Короткий огляд змісту книги, статті - анотація, Короткий перелік проблем досліджуваних у науковому тексті - план, Стислий писаний виклад змісту наукової праці - конспект, Коротко сформульовані шото там - Тези")
    elif message.text == '23':
        bot.send_message(message.chat.id, text="переказ змісту тексту оригіналу мовою який не ставить за мету відтворення мовних засобів оригіналу - вільний, стисла характеристика оригіналу є переліком основних питань - анотаційний, переклад заздалегідь відібраних частин оригіналу, що складають звязний текст - реферативний, переклад слово в слово - буквальний")
    elif message.text == '24':
        bot.send_message(message.chat.id, text="власне українські слова - слухач, мрія, завдяки, спросоння, хуртовина, загальновживані - Рука, нога, голова, термінологічні - суфікс, префікс, дифузія, запозичені - адміністрація, депутат, автономія ")
    elif message.text == '25':
        bot.send_message(message.chat.id, text="офіційно-ділова лексика - декларація, угода, протокол, номенклатурні назви - долар, Чорне море, заєць-біляк, Термінологічні - валюта, стиль, валентність, професіоналізми - клава, фанера, скинути інформацію, підвал, вікно")
    elif message.text == '26':
        bot.send_message(message.chat.id, text="")    
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
