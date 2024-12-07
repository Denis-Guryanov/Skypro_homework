import os
import requests
from dotenv import load_dotenv

def get_currency(from_cur, to_cur, amount):
    '''Функция конвертации транзакции с использованием API'''
    load_dotenv()
    apikey = os.getenv('API_KEY')
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_cur}&from={from_cur}&amount={amount}"

    headers = {"apikey": apikey}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"{response.status_code}")
    else:
        data = response.json()
        amount = round(data["result"], 2)
        return amount


if __name__ == "__main__":
    print(get_currency("RUB", "USD", 10000))