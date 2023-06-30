import os
import requests
from getUpdates import get_updates

TOKEN = '6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'

def sendMessage(chat_id:str, text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    paramters = {
        'chat_id':chat_id,
          'text':text
          }
    response = requests.get(URL, params=paramters)
    return response.json()
m=0
while True:
    x=get_updates(TOKEN)
    if len(x)!=m:
        text = get_updates(TOKEN)[-1]['message']['text']
        chat_id = get_updates(TOKEN)[-1]["message"]["chat"]['id']
        sendMessage(chat_id=chat_id, text=text)
        print(text)
        m=len(x)