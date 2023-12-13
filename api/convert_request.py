import requests
import configparser

class Converter:

    def __init__(self):
        """
        Инициализация данных
        """

        parser = configparser.ConfigParser()
        parser.read('../auth.ini')
        API_KEY = "".join(filter(lambda word: word not in "\'\"", parser.get('auth', "API_KEY")))
        SITE = "".join(filter(lambda word: word not in "\'\"", parser.get('auth', "SITE")))
        data = requests.get(str(SITE)+"".join(list(filter(lambda word: word not in ['\"', "\'"], API_KEY)))).json()

        #Список всех валют
        self.all_rates = set(data["rates"].keys())
