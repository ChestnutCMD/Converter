# Конвертор валют. Принимает код двух валют и количество обмениваемой валюты

import requests
from bs4 import BeautifulSoup


class Converter:
    url = "https://www.banki.ru/products/currency/cb/"  # сайт с которого берутся курсы валют

    def __init__(self, from_exchange, to_exchange, value):
        self.from_exchange = from_exchange
        self.to_exchange = to_exchange
        self.value = value

    @staticmethod
    def __parse(url):
        """Парсинг с сайта"""
        req = requests.get(url)
        src = req.text
        return BeautifulSoup(src, "lxml")

    def __parse_filter(self, country_code) -> list:
        """Фильтрация валюты по ее коду, возвращает курс в рублях"""
        soup = self.__parse(self.url)
        countries = soup.find('tr', {"data-currency-code": country_code.upper()})
        result = countries.text.split()
        return result

    def calculation(self):
        """Калькулятор валюты"""
        try:
            from_cash = self.__parse_filter(self.from_exchange)
            to_cash = self.__parse_filter(self.to_exchange)
            result = round(float(from_cash[-2]) * float(self.value) / float(to_cash[-2]), 2)
        except AttributeError:
            result = "Код валюты не найден"
        return result
