import os
import requests
from getUpdates import get_updates, last_update_id
from time import sleep

TOKEN = '6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'

def sendMessage(chat_id:str, text:str):

    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    paramters = {'chat_id':chat_id, 'text':text}

    response = requests.get(URL, params=paramters)
    return response.json()

last_id = -1

while True:
    update = get_updates(TOKEN)
    last_update = update[-1]
    update_id = last_update_id(update)
    if last_id != update_id:
        text = last_update['message']['text']
        chat_id = last_update["message"]["chat"]['id']

        sendMessage(chat_id=chat_id, text=text)
        print(text)

        last_id =update_id
