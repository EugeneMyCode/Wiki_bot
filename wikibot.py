import telebot, wikipedia, re

bot = telebot.TeleBot('5069779543:AAEfOdCA3SEW0uJpo7FP_9Ztvjrl1Qf-xks')

wikipedia.set_lang('ru')

def wikiget(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for i in wikimas:
            if not('==' in i):
                if(len((i.strip()))>3):
                    wikitext2 = wikitext2+i+'.'
            else:
                break

        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    
    except Exception as e:
        return 'Увы, в википедии нет информации о вашем запросе.'

@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Давай сюда слово, найду его в Википедии!')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, wikiget(message.text))

bot.polling(none_stop=True, interval=0)
    