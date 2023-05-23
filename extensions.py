#coding=utf-8
import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class get_price():
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести {base} в {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'{quote} валюту не обрабатываю.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'{base} не обрабатываю.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'{amount} не могу столько обрабатывать.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base