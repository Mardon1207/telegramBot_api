import os 
import requests
from getUpdates import get_updates

TOKEN = '6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'

def sendPhoto(chat_id:str,photo:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    paramters = {
        'chat_id':chat_id,
        'photo':photo
        }
    response = requests.get(URL, params=paramters)
    return response.json()
m=0
while True:
    x=get_updates(TOKEN)
    if len(x)!=m:
        photo = get_updates(TOKEN)[-1]['message']['photo'][0]['file_id']
        chat_id = get_updates(TOKEN)[-1]["message"]["chat"]['id']
        sendPhoto(chat_id=chat_id, photo=photo)
        print(photo)
        m=len(x)




# photo_url='https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg'
# photo_id = 'AgACAgIAAxkDAAMgY7evYvSyDJQ8DS-1S5Irjcd9cIgAAoa_MRvjDsFJ4H7lvD-PEXwBAAMCAAN4AAMtBA'
# img = open('logo.jpg','rb').read()


# send photo with three ways: url, id, file
