import tkinter

from tkinter import ttk
from api.convert_request import Converter


class Application:

    def __init__(self):
        """
        Инициализация данных
        """
        self.app = tkinter.Tk()
        self.app.title("Converter")

        #Объект класса конвертёр
        self.converter = Converter()

    def create_widgets(self):
        """
        Создание виджетов
        :return:
        """

        # Метки
        label_1 = tkinter.Label(self.app, text="Что конвертировать", font="arial 10", borderwidth=10)
        label_2 = tkinter.Label(self.app, text="Сумма конвертации", font="arial 10", borderwidth=10)
        label_3 = tkinter.Label(self.app, text="Во что конвертировать", font="arial 10", borderwidth=10)
        label_4 = tkinter.Label(self.app, text="Итоговая сумма", font="arial 10", borderwidth=10)

        # Выпадающие списки
        cmbox_1 = ttk.Combobox(self.app, values=self.converter.get_all_rates())
        cmbox_2 = ttk.Combobox(self.app, values=self.converter.get_all_rates())

        #Поле суммы конвертации
        entry_all_money = tkinter.Entry(self.app)

        # Поле вывода
        entry_answer = tkinter.Entry(self.app)

        # Установка кнопки
        button_check = tkinter.Button(text="Рассчитать", font="arial 10", borderwidth=3)

        # Установка объектов
        label_1.grid(row=0, column=0)
        cmbox_1.grid(row=0, column=1)

        label_2.grid(row=1, column=0)
        entry_all_money.grid(row=1, column=1)

        label_3.grid(row=2, column=0)
        cmbox_2.grid(row=2, column=1)

        button_check.grid(row=3, columnspan=2)
        label_4.grid(row=4, column=0)

        entry_answer.grid(row=4, column=1)

    def display_appliction(self):
        """
        Запуск приложения
        :return:
        """
        self.create_widgets()
        self.app.mainloop()

    def __str__(self):
        return "Class application.\nCreated applicaion and do convert values"

