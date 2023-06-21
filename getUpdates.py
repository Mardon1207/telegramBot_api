import requests

def get_updates(TOKEN):
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


    response = requests.get(url=BASE_URL)
    updates=response.json()['result']
    return updates
# print each update

def last_update_id(update):
    updates=update[-1]['update_id']
    return updates
