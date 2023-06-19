import requests

TOKEN = '6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


response = requests.get(url=BASE_URL)
updates=response.json()['result']
# print each update
print(updates)
