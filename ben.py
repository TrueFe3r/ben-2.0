
from telethon import events
import requests
from uniborg.util import admin_cmd
import random as rd 

@borg.on(admin_cmd("ben2"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    num = rd.randint(1, 4)
    if num == 1:
        m = "Бен говорит: Да."
    if num == 2:
        m = "Бэн говорит: Нет."
    if num == 3:
    	m = "Бэн говорит: Ха-ха-ха!"
    if num == 4:
    	m = "Бэн говорит: Фу-у-у..."
    await borg.send_message(
        event.chat_id,
        m,
        reply_to=message_id
    )
    await event.delete()
    #Бэн, когда?
@borg.on(admin_cmd("benwhen"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    num = rd.randint(1, 10)
    age = rd.randint(25, 120)
    if num == 1:
        m = "Бен говорит: Через 10 минут."
    if num == 2:
        m = "Бэн говорит: Через неделю."
    if num == 3:
    	m = "Бэн говорит: Завтра."
    if num == 4:
    	m = "Бэн говорит: Никогда..."
    if num == 5:
    	m = "Бэн говорит: Не уверен, спроси позже."
    if num == 6:
    	m = "Бэн говорит: Скоро."
    if num == 7:
    	m = "Бэн говорит: Послезавтра."
    if num == 8:
    	m = "Бэн говорит: Через месяц-полтора."
    if num == 9:
    	m = "Бэн говорит: Вчера."
    if num == 10:
        m = "Бэн говорит: когда тебе стукнет " + str(random.randint(25, 120)
    await borg.send_message(
        event.chat_id,
        m,
        reply_to=message_id
    )
    await event.delete()
