import requests
import configparser

from typing import Mapping

class Converter:

    def __init__(self):
        """
        Инициализация данных
        """

        parser = configparser.ConfigParser()
        parser.read('auth.ini')

        #Данные АПИ сервиса
        self.__API_KEY = "".join(filter(lambda word: word not in "\'\"", parser.get('auth', "API_KEY")))
        self.SITE = "".join(filter(lambda word: word not in "\'\"", parser.get('auth', "SITE")))

        self.data = requests.get(self.SITE+"/latest?access_key="+self.__API_KEY).json()

        #Список всех валют
        self.__all_rates = sorted(set(self.data["rates"].keys()))

    def get_all_rates(self) -> list:
        """
        Возвращает список всех валют
        :return:
        """
        return list(self.__all_rates)

    def convert_values(self, type_val_1: str, type_val_2: str, value: Mapping[float, int]):
        """
        Метод конвертации валют
        :param type_val_1:
        :param type_val_2:
        :param value:
        :return:
        """

        initial_value = value
        if type_val_1 != "EUR":
            initial_value = initial_value / self.data["rates"][type_val_1]
        result = initial_value * self.data["rates"][type_val_2]

        result = round(initial_value * self.data["rates"][type_val_2], 2)
        return str(result)



    def __str__(self):
        return "Class Converter.\nreturn: all_rates, convert currencies"