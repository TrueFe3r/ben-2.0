""" Бен на МАКСИМАЛКАХ!))
Команда: .ben автор @ToxicUse"""
from telethon import events
import requests
from uniborg.util import admin_cmd
import random as rd

@borg.on(admin_cmd("ben"))
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
    #Зачем ты это читал 
