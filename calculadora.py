from tkinter import *
from tkinter import messagebox

tela = Tk()
tela.geometry('250x300')
tela.title("Calculadora")


#campo calc
campo = Entry(tela, width=20, font=('Arial', 15), bd=10)
campo.grid(column=1, row=0, padx=2)

def lim():
    try:
        text = campo.get()
        resultado = eval(text)
        campo.delete(0, END)
        campo.insert(0, resultado)
    except EOFError:
        messagebox.showerror('Error na espressão')


def clear():
    campo.delete(0, END)


def eu():
    messagebox.showinfo("criador", "Fabiano Batista")


#botões
b1 = Button(tela, text='1', font=('Arial', 15, 'bold'), width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '1'))
b1.grid(column=1, row=3, padx=2, sticky='W')

b2 = Button(tela, text='2', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '2'))
b2.grid(column=1, row=3, padx=2, sticky='N')

b3 = Button(tela,  text='3', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '3'))
b3.grid(column=1, row=3, padx=2, sticky='E')

b4 = Button(tela, text='4', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '4'))
b4.grid(column=1, row=4, padx=2, sticky='W')

b5 = Button(tela, text='5', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '5'))
b5.grid(column=1, row=4, padx=2, sticky='N')

b6 = Button(tela, text='6', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '6'))
b6.grid(column=1, row=4, padx=2, sticky='E')

b7 = Button(tela, text='7', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '7'))
b7.grid(column=1, row=5, padx=2, sticky='W')

b8 = Button(tela, text='8', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '8'))
b8.grid(column=1, row=5, padx=2, sticky='N')

b9 = Button(tela, text='9', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '9'))
b9.grid(column=1, row=5, padx=2, sticky='E')

b0 = Button(tela, text='0', font=('Arial', 15, 'bold'), width=5, height=1, relief='solid',
            command=lambda: campo.insert(END, '0'))
b0.grid(column=1, row=6, padx=2, sticky='W')

bsum = Button(tela, text='+', font=('Arial', 15, 'bold'),  width=5, height=1, relief='solid',
              command=lambda: campo.insert(END, '+'))
bsum.grid(column=1, row=6, padx=2, sticky='N')

bsub = Button(tela, text='-',  font=('Arial', 15, 'bold'),  width=5, height=1,relief='solid',
              command=lambda: campo.insert(END, '-'))
bsub.grid(column=1, row=6, padx=2, sticky='E')

butcalc = Button(tela, text='=',  font=('Arial', 15, 'bold'),  width=5, height=1,relief='solid',
                 command=lambda: lim())
butcalc.grid(column=1, row=7, padx=2, sticky='W')

butmult = Button(tela, text='X',  font=('Arial', 15, 'bold'),  width=5, height=1,relief='solid',
                 command=lambda: campo.insert(END, '*'))
butmult.grid(column=1, row=7, padx=2, sticky='N')

butdiv = Button(tela, text='÷', font=('Arial', 15, 'bold'),  width=5, height=1,relief='solid',
                command=lambda: campo.insert(END, '/'))
butdiv.grid(column=1, row=7, padx=2, sticky='E')

butlimp = Button(tela, text='C', font=('Arial', 15, 'bold'),  width=5, height=1,relief='solid',
                 command=lambda: clear())
butlimp.grid(column=1, row=8, padx=2, sticky='N')

butcredts = Button(tela, text='criador', font=('Arial', 15, 'bold'),  width=5, height=1, relief='flat',
                   command=lambda: eu())
butcredts.grid(column=1, row=8, padx=2, sticky='E')

tela.mainloop()
