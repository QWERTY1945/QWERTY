from token import token 
import telebot 

bot = telebot.TeleBot((token["TOKEN"]))

@bot.messedge_hendler(comands=["start"])
def start(messedge):
    bot.send_messedge(messedge.chat.id, "Как тебя зовут?")


@bot.messedge_hendler(comands=["text"])
def start(messedge):
    msg=bot.send_messedge(messedge.chat.id, f"Привет, {messedge.text}")
    # bot.register_next_step_handler(msg, name)








if_name_='__main__':
    bot.polling(name_stop=True)





















# print(token["TOKEN"])

