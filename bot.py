import telebot
from epic import get_xi as xii

API_TOKEN='这里写token'
bot=telebot.TeleBot(API_TOKEN,parse_mode='MARKDOWN')

@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    bot.reply_to(message,'使用 /epic 指令获取喜加一信息')

@bot.message_handler(commands=['epic'])
def send_welcome(message):
    xi=xii()
    if len(xi)==2:
        bot.reply_to(message,'本周喜加二🎉!')
    elif len(xi)==1:
        bot.reply_to(message,'本周喜加一🌈!')
    for x in xi:
        bot.reply_to(message,'🌈游戏名: %s\n⚡截止日期: %s (开始于 %s)\n🔥是否永久: %s!\n🎁来自: [%s](%s)'%(x['name'],x['end_time'],x['start_time'],x['forever'].replace('yes','是').replace('no','不是'),x['via'],x['link']))

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message,message.text)

bot.infinity_polling()