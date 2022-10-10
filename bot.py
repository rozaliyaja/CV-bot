#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'Вставьте свой токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('hello boys.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🤓 Мой репозиторий")
	item2 = types.KeyboardButton("📝 Написать мне в личку")
	item3 = types.KeyboardButton("📂 Посмотри мое резюме на hh")
	item4 = types.KeyboardButton("📱 Позвони мне")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Привет тебе от милого и смешного человека, ну и, конечно же, классного QA, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🤓 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/rozaliyaja')
		elif message.text == '📝 Написать мне в личку':
			bot.send_message(message.chat.id, 'http://t.me/rozaliyaja')
		elif message.text == '📂 Посмотри мое резюме на hh': 
			bot.send_message(message.chat.id, 'https://kazan.hh.ru/resume/59535cdbff02f6ded60039ed1f657369566a5a')
		elif message.text == '📱 Позвони мне':
			bot.send_message(message.chat.id,  "+79172281502", reply_markup=start_keyboard)	
		else:
			bot.send_message(message.chat.id, 'Тыкни в любую другую кнопку :)')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods