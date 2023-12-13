import tkinter

app = tkinter.Tk()
app.title("Конвертёр валют")
label_1 = tkinter.Label(app, text="Сумма конвертации", font="arial 10", borderwidth=10)
label_2 = tkinter.Label(app, text="Что конвертировать", font="arial 10", borderwidth=10)
label_3 = tkinter.Label(app, text="Во что конвертировать", font="arial 10", borderwidth=10)
label_4 = tkinter.Label(app, text="Итоговая сумма", font="arial 10", borderwidth=10)

entr_1 = tkinter.Entry(app)
entr_2 = tkinter.Entry(app)
entr_3 = tkinter.Entry(app)
entr_4 = tkinter.Entry(app)

button = tkinter.Button(app, text="Рассчитать", font="arial 10", borderwidth=4)

label_1.grid(row=0, column=0)
entr_1.grid(row=0, column=1)
label_2.grid(row=1, column=0)
entr_2.grid(row=1, column=1)
label_3.grid(row=2, column=0)
entr_3.grid(row=2, column=1)
button.grid(row=3, columnspan=2)
label_4.grid(row=4, column=0)
entr_4.grid(row=4, column=1)

app.mainloop()
