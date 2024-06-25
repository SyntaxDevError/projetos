from tkinter import *
from random import randint
from time import sleep
from tkinter import messagebox


def jokenpo():
    def contagem():
        campo.config(text=f'Calculando resultado...')
        jan_jokenpo.update()
        jan_jokenpo.after(5000)
        
    def pedra():
        contagem()
        jogadas = ['Pedra', 'Papel', 'Tesoura']
        computador = randint(0, 2)
        jogo_cpu = jogadas[computador]

        if jogo_cpu == 'Pedra':
            messagebox.showinfo("Empate", f"O jogador escolheu Pedra e o adversário escolheu {jogo_cpu}")
            campo.config(text='Faça sua escolha...')
        elif jogo_cpu == 'Papel':
             messagebox.showinfo("Vitoria!!!", f"O jogador escolheu Pedra e o adversário escolheu {jogo_cpu}")
             campo.config(text='Faça sua escolha...')
        elif jogo_cpu == 'Tesoura':
             messagebox.showinfo("Derrota!!!", f"O jogador escolheu Pedra e o adversário escolheu {jogo_cpu}")
             campo.config(text='Faça sua escolha...')
        else:
            messagebox.showerror("problemas", "Erro ao carregar minegame")
            campo.config(text='Faça sua escolha...')
    
    def papel():
        contagem()
        jogadas = ['Pedra', 'Papel', 'Tesoura']
        computador = randint(0, 2)
        jogo_cpu = jogadas[computador]

        if jogo_cpu == 'Pedra':
            messagebox.showinfo("Vitória!!!", f"O jogador escolheu Papel e o adversário escolheu {jogo_cpu}")
            campo.config(text='Faça sua escolha...')
        elif jogo_cpu == 'Papel':
             messagebox.showinfo("Empate", f"O jogador escolheu Papel e o adversário escolheu {jogo_cpu}")
             campo.config(text='Faça sua escolha...')
        elif jogo_cpu == 'Tesoura':
             messagebox.showinfo("Derrota!!!", f"O jogador escolheu Papel e o adversário escolheu {jogo_cpu}")
             campo.config(text='Faça sua escolha...')
        else:
            messagebox.showerror("problemas", "Erro ao carregar minegame")
            campo.config(text='Faça sua escolha...')
    
    def tesoura():
        contagem()
        jogadas = ['Pedra', 'Papel', 'Tesoura']
        computador = randint(0, 2)
        jogo_cpu = jogadas[computador]

        if jogo_cpu == 'Pedra':
            messagebox.showinfo("Derrota", f"O jogador escolheu Tesoura e o adversário escolheu {jogo_cpu}")
            campo.config(text='Faça sua escolha...')
        elif jogo_cpu == 'Papel':
             messagebox.showinfo("Vitória!!!", f"O jogador escolheu Tesoura e o adversário escolheu {jogo_cpu}")
             campo.config(text='Faça sua escolha...')
        elif jogo_cpu == 'Tesoura':
             messagebox.showinfo("Empate", f"O jogador escolheu Tesoura e o adversário escolheu {jogo_cpu}")
             campo.config(text='Faça sua escolha...')
        else:
            messagebox.showerror("problemas", "Erro ao carregar minegame")
            campo.config(text='Faça sua escolha...')






    jan_jokenpo = Tk()
    jan_jokenpo.title("JOKENPO!")

    back = Button(jan_jokenpo, text='Voltar', fg='white', bg='red', command=lambda: jan_jokenpo.destroy()).grid(column=0, row=0, sticky='W')
    campo = Label(jan_jokenpo, text='Faça sua Escolha...', font=('arial', 28), width=18, height=7)
    campo.grid(column=0, row=1, columnspan=3, pady=20)

    but_pedra = Button(jan_jokenpo, text='Pedra', command=pedra, width=10, height=4).grid(column=0, row=2, pady=20)
    but_papel = Button(jan_jokenpo, text='Papel', command=papel, width=10, height=4).grid(column=1,row=2, pady=20)
    but_tesoura = Button(jan_jokenpo, text='Tesoura', command=tesoura, width=10, height=4).grid(column=2, row=2, pady=20)


    jan_jokenpo.mainloop()

janela_principal = Tk()
janela_principal.title('Jogos vc computador...')

close = Button(janela_principal, text="X", fg='white', bg='red', command=lambda: janela_principal.destroy()).grid(column=0, row=0, sticky="w")
ppt = Button(janela_principal, text='JOKENPO', command=jokenpo).grid(column=0, row=1)


janela_principal.mainloop()