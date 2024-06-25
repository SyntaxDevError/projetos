from tkinter import *
import datetime
from teste import cro

contando = False
valor = 0

def Hora():
    atual = datetime.datetime.now()
    hora = atual.time().hour
    min = atual.time().minute
    seg = atual.time().second

    campo_show.config(text=f'{hora:02}:{min:02}:{seg:02}')
    jan.after(1000, Hora)





jan = Tk()
jan.title("Relógio")
jan.geometry('460x380')

campo_show = Label(jan, text='', font=('Melvetica', 86))
campo_show.grid(column=0, row=0, pady=20)
Hora()
bot_cro = Button(jan, text='Cronometro', command=cro)
bot_cro.grid(column=0, row=1)

jan.mainloop()
