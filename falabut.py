from tkinter import *
from gtts import gTTS
import playsound
import os

def speak():
    texto = campo.get()

    arquivo = "audioescrito.mp3"
    sla = gTTS(texto, lang='pt')
    sla.save(arquivo)

    playsound.playsound("audioescrito.mp3")
    janela.update()
    os.remove(arquivo)

janela = Tk()
janela.geometry('340x340')

campo = Entry(janela, font=("arial", 20), bd=5)
campo.grid(pady=30, padx=11)

butfala = Button(janela,text="falar",width=10, height=4,font=('arial', 9), command=speak)
butfala.grid()

janela.mainloop()