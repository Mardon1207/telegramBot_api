import requests

TOKEN = '6031625012:AAFdxBk9YBo_m2U4llpFUk854ZoLXTPWSZ0'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'


response = requests.get(url=BASE_URL)
if response.status_code == 200:
    info = response.json()
    print(info)