#!/usr/bin/python3
import sys
import time
import telepot
from telepot.loop import MessageLoop
import requests

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type,chat_type,chat_id)

    if content_type == 'text' and msg['text'] == '/yolo':
        r = requests.get('https://get.yolo.jetzt')
        i = int(r.text)
        if i > 9000:
            bot.sendMessage(chat_id, 'OVER NINETHOUSAND!!!')
        else:
            bot.sendMessage(chat_id, r.text)

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
