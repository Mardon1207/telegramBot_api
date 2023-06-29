import os
import requests
from getUpdates import get_updates
TOKEN = '6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'

def sendMessage(chat_id:str, text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    kb1={
        'text':"Yes,they certainly are"
    }
    kb2={
        'text':"I'm not quite sure"
    }
    kb3={
        'text':"No !"
    }
    keyboard=[[kb1],[kb2],[kb3]]
    keyboard={
        'keyboard':keyboard,
        'resize_keyboard':True
    }
    parametrs={
        'chat_id':chat_id,
        'text':text,
        "reply_markup":keyboard
    }
    response=requests.post(URL,json=parametrs)
    return response.json()
chat_id = get_updates(TOKEN)[-1]["message"]["chat"]['id']
print(sendMessage(chat_id,'keybord'))
