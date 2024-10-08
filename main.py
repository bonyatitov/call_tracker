import telebot 
import secret

bot = telebot.TeleBot(secret.TOKEN) # Getting a bot token

answer_opt_for_price = ['Прайс', 'прайс', 'ghfqc', 'Ghfqc']
answer_opt_for_date = ['Календарь', 'календарь', 'Rfktylfhm', 'rfktylfhm']
answer_opt_for_record = ['Да', 'да', 'lf', 'Lf']

# For user data 

user_name = ''   
user_phone = ''


def message_contain (message, arr):
    for answer in arr:
        if message == answer:
            return True

        


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Здравствуйте, записать вас на прием? напишите - Да\nЕсли хотите узнать цену приема, напишите - Прайс\nДни в которые можно записаться, напишите - Календарь')
    elif message_contain(message.text, answer_opt_for_price):
        bot.send_message(message.from_user.id, 'Этот пункт пока в разработке')
    elif message_contain(message.text, answer_opt_for_date):
        bot.send_message(message.from_user.id, 'Этот пункт пока в разработке')
    elif message_contain(message.text, answer_opt_for_record):
        bot.send_message(message.from_user.id, 'Как вас зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю. напишите /help')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Напишите номер телефона')
    bot.register_next_step_handler(message, get_number)

def get_number (message):
    global phone_number
    phone_number = message.text 
    bot.send_message(message.from_user.id, 'Спасибо за информацию! Я свяжусь с вами в течении 15 минут для подтверждения записи.')




bot.polling(none_stop=True, interval=0)



