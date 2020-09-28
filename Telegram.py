import telebot
print('Бот запущен')
token = '1236967730:AAFuqqk4fQ4YF-UihQRVZJaUSohCxenWDuM'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Добро пожаловать, мой господин!')

@bot.message_handler(content_types=['text'])
def send_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,'Здравствуйте')
    elif message.text.lower() == 'как дела':
        bot.send_message(message.chat.id,'Крутоооо, а у тебя? как?)')
    elif message.text.lower() == 'отлично':
        bot.send_message(message.chat.id,'Так держать!')
    elif message.text.lower() == 'хорошо':
        bot.send_message(message.chat.id,'Кто бы сомневался!')
    elif message.text.lower() == 'что опять у нави':
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMZX3HjfFjiElk7RTquh3NoFM0mUkcAAhcAA1oeUBXAT-kgYI5TmBsE')
    elif message.text.lower() == 'россия выиграла чм по футболу':
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMvX3HngtAmnPrgSrntWGf9hkCZJeMAAgcAA3j6-xeEQS1PHCGHuhsE')
    elif message.text.lower() == 'кого выиграли':
        bot.send_message(message.chat.id,'Бразилию 3-0')
    elif message.text.lower() == 'ничоси':
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMyX3Ho2tf4JQABfs05VMLiqG5EsKddAAIRAAN4-vsXKlCpFD9P4rEbBA')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)

bot.polling()
