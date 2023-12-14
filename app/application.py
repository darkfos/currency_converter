import tkinter

from tkinter import ttk
from api import api_request
from typing import Mapping

class Application:

    def __init__(self):
        """
        Инициализация данных
        """
        self.app = tkinter.Tk()
        self.app.title("Converter")

        #Объект класса конвертёр
        self.converter = api_request.Converter()


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
        self.cmbox_1 = ttk.Combobox(self.app, values=self.converter.get_all_rates())
        self.cmbox_2 = ttk.Combobox(self.app, values=self.converter.get_all_rates())

        #Поле суммы конвертации
        self.entry_all_money = tkinter.Entry(self.app)

        # Поле вывода
        self.entry_answer = tkinter.Entry(self.app)

        # Установка кнопки
        button_check = tkinter.Button(text="Рассчитать", font="arial 10", borderwidth=3, command= lambda:
            self.click_button('EUR' if self.cmbox_1.get() == '' else self.cmbox_1.get(),
                              'EUR' if self.cmbox_2.get() == '' else str(self.cmbox_2.get()),
                              0 if self.entry_all_money.get() == '' else float(self.entry_all_money.get())))

        # Установка объектов
        label_1.grid(row=0, column=0)
        self.cmbox_1.grid(row=0, column=1)

        label_2.grid(row=1, column=0)
        self.entry_all_money.grid(row=1, column=1)

        label_3.grid(row=2, column=0)
        self.cmbox_2.grid(row=2, column=1)

        button_check.grid(row=3, columnspan=2)
        label_4.grid(row=4, column=0)

        self.entry_answer.grid(row=4, column=1)

    def display_appliction(self):
        """
        Запуск приложения
        :return:
        """
        self.create_widgets()
        self.app.mainloop()

    def click_button(self, cmbox_1: str, cmbox_2: str, entry_all_money: Mapping[float, int]):
        self.entry_answer.delete(0, len(self.entry_answer.get()))
        result = self.converter.convert_values(cmbox_1, cmbox_2, entry_all_money)
        self.entry_answer.insert(string=result, index=0)


    def __str__(self):
        return "Class application.\nCreated applicaion and do convert values"

