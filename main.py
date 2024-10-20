import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        attacker_username = message.from_user.username
        defender_username = message.reply_to_message.from_user.username
        if attacker_username in Pokemon.pokemons and defender_username in Pokemon.pokemons:
            result = attack(attacker_username, defender_username)
        else:
           bot.send_message(message, "Один из пользователей не имеет покемона для сражения!")


                        
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для игры в покемонов, скорее попробуй создать себе покемона, нажимай - /go")


bot.infinity_polling(none_stop=True)

