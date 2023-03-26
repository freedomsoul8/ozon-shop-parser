import telebot
from other import Shop
from parser import load_shop_page, get_product_cards

bot = telebot.TeleBot(token="5875749712:AAGDiP8ZZYZ0Fi0wF2u65w0hSkU3vvl-sqk")

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id,text='Отправьте ссылку на магазин Ozon')
    bot.register_next_step_handler(msg, recive_url)
def recive_url(message):
    message.text = Shop.url
    elements = get_product_cards(page=load_shop_page(url=Shop.url))
    for element in elements:
        bot.send_message(message.chat.id,text=element)


if __name__ == "__main__":
    bot.polling(none_stop=True)