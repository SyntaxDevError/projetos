from tkinter import *
from random import randint
from time import sleep
from tkinter import messagebox

def dados_game():
    def manual():
        messagebox.showinfo("Manual de instruções",""" Digite no campo de entrada um valor situado entre 1 e 6
                   Caso informe um valor nulo, palavra ou caracter específico dará erro no jogo
                   Logo após aperte o botão play e o jogo funcionara caso esteja nas condições ideais
                   A cada rodada será ranomizado um valor novamente, ou seja, a cada play mudara o valor do cpu
                   divirta-se""")
    
    def palp():
        try:
            valor = campo_entrada.get()
            valor1 = valor.replace(" ", "")
            valor2 = int(valor1)
        except TypeError as tipo:
            messagebox.showerror("Error", "Digite um número inteiro")
        except:
            messagebox.showerror("Error", "Erro ao digitar o valor")
        else:
            if valor2 != '':
                if 0 < valor2 < 7 :
                    campo.config(text='Calculando resultado...')
                    play.config(state="disabled")
                    dadosJan.update()
                    dadosJan.after(3000)
                    play.config(state='active')
                    cpu = randint(1, 6)
                    if valor2 == cpu:
                        campo.config(text=f"Acertou!!\nO computador jogou {cpu}\nO seu palpite foi {valor2}  ")
                    else:
                        campo.config(text=f'Errou...\nO computador jogou {cpu}\nO seu palpite foi {valor2}')
                else:
                    messagebox.showerror("valor número", "Digite um número entre 1 e 6!")
        


    dadosJan = Tk()
    dadosJan.title("jogo dos dados")
    dadosJan.geometry("460x380")

    butback = Button(dadosJan, text='<--', fg='white', bg='red', command=lambda: dadosJan.destroy()).grid(column=0, row=0)
    butinst = Button(dadosJan, text='Instruções', bg='blue', fg='white', command=manual).grid(column=1, row=0)

    campo = Label(dadosJan, text='Jogo dos dados',width=20 ,height=6 , font=('roboto', 15))
    campo.grid(column=0, row=1, columnspan=2)


    text_label = Label(dadosJan, text="Digite seu palpite entre 1 a 6:", font=('Roboto', 10, 'bold')).grid(column=0, row=2, columnspan=2, sticky='N')
    campo_entrada = Entry(dadosJan, width=20, font=('roboto', 20, 'bold'))
    campo_entrada.grid(column=0, row=3, columnspan=2, sticky="W")
    play = Button(dadosJan, text='Play', command=palp, width=12, height=2)
    play.grid(column=0, row=4, sticky='W')


    dadosJan.mainloop()


def jokenpo():
    def contagem():
        campo.config(text=f'Calculando resultado...')
        jan_jokenpo.update()
        jan_jokenpo.after(3000)
        
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

larg, alt = 20, 4

close = Button(janela_principal, text="X", fg='white', bg='red', command=lambda: janela_principal.destroy()).grid(column=0, row=0, sticky="w")
ppt = Button(janela_principal, text='JOKENPO', command=jokenpo, width=larg, height=alt).grid(column=0, row=1, pady=20)
jogo_dados = Button(janela_principal, text="Jogo dos dados", command=dados_game, width=larg, height=alt).grid(column=0, row=2, pady=20)

janela_principal.mainloop()