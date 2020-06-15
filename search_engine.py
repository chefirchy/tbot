## Краткий синтаксис ожидаемого языка разметки для бота
## строка, которая начинается с @ - заголовок
## Все что в __здесь__ - это важный текст
import re

# Функция принимает как аргумент текст, который следует искать, и массив с сообщений, в которых нужно искать
def get_best_match(text, messages = []):
  score_of_best_match = 0
  best_match_index = None

  i = 0
  for message in messages:
    header_apearances_count = get_header_appearances(text, message)
    bold_appearances_count = get_bold_appearances(text, message)
    common_appearances_count = get_appearances(text, message) - bold_appearances_count - header_apearances_count
    
    if header_apearances_count != 0:
      best_match_index = i
      break
    if bold_appearances_count * 2.5 + common_appearances_count > score_of_best_match:
      score_of_best_match = bold_appearances_count * 2.5 + common_appearances_count
      best_match_index = i

    i += 1
  
  return format_text(text, messages[best_match_index])

# Возвращает количество text в message помеченных как заголовки c помощью @
def get_header_appearances(text, message):
  appearances = re.findall(rf'.*\@.*{text}?', message, flags = re.IGNORECASE)
  return len(appearances)

# Возвращает количество text в message
def get_appearances(text, message):
  return message.lower().count(text.lower())    
# Возвращает количество text в message условно выделенных с помощью __ __
def get_bold_appearances(text, message):
  appearances_count = 0
  boldText = re.findall(r'\_\_.*?\_\_', message, flags = re.IGNORECASE | re.MULTILINE)
  for bold in boldText:
    appearances_count += bold.lower().count(text.lower())
  return appearances_count

# Функция выделяет в message text с помощью ** **, а также удаляет символы @
def format_text(text, message):
  header_less = message.replace('@', '')
  bolded = re.sub(rf'({text})', r'**\1**', header_less, flags=re.IGNORECASE)
  return bolded