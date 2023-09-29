import tkinter as tk
from tkinter import messagebox
import random

#def as config do jogo

num_linhas = 4
num_colunas= 4
cartao_size_w = 10
cartao_size_h = 5

cores_cartao = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'white', 'magenta'] 
cor_fundo = '#8B4513'
cor_letra = '#FFDEAD'
font_style = ('Arial', 12, 'bold')
max_tentativas = 20

# Cria uma grade aleatoria de cores para os cartões

def create_card_grid():
    cores = cores_cartao *2
    random.shuffle(cores)
    grid = []
    
    for _ in range(num_linhas):
        linha = []
        for _ in range(num_colunas):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

# Lidar com os eventos de click
def card_clicked(linha, coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor == '#F4A460':
        cartao['bg'] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_match()    

# Verificar se os dois cartões revelados são iguais
def check_match():
    cartao1, cartao2 = cartao_revelado
    if cartao1['bg'] == cartao2['bg']:
        cartao1.after(1000, cartao1.destroy)
        cartao2.after(1000, cartao2.destroy)
        cartao_iguais.extend([cartao1, cartao2])
        check_win()
    else:
        cartao1.after(1000, lambda: cartao1.config(bg='#F4A460'))
        cartao2.after(1000, lambda: cartao2.config(bg='#F4A460'))
    cartao_revelado.clear()
    update_score()


# Verificar se o jogador ganhou
def check_win():
    if len(cartao_iguais) == num_linhas * num_colunas:
        messagebox.showinfo('Parabéns', 'Você ganhou um beijo.')
        janela.quit()

# Atualiza a pontuação e verifica se o jogador perdeu
def update_score():
    global num_tentativas
    num_tentativas += 1
    label_tentativas.config(text='Tentativas: {}/{}'.format(num_tentativas, max_tentativas))
    if num_tentativas >= max_tentativas:
        messagebox.showinfo('Derrota', 'Lixo!')
        janela.quit()

# Criando a interface principal

janela = tk.Tk()
janela.title('Jogo Da Memoria do Gostosão do italo')
janela.configure(bg=cor_fundo)


# Criar grade de cartões
grid = create_card_grid()
cartoes = []
cartao_revelado = []
cartao_cores = []
cartao_iguais = []
num_tentativas = 0


for linha in range(num_linhas):
    linha_de_cartoes = []
    for col in range(num_colunas):
        cartao = tk.Button(
            janela, command=lambda r=linha, c=col: card_clicked(r, c),
             width=cartao_size_w, height= cartao_size_h, bg='#F4A460', relief=tk.RAISED, bd=3
             )
             
        cartao.grid(row=linha, column=col, padx=5, pady=5)
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)


# personalizando botão
button_style = {
    'activebackground': "#483D8B", 'font': font_style, "fg":cor_letra
    }
janela.option_add('*Button', button_style)

# label para numero de tentavias
label_tentativas = tk.Label(
    
    janela, text='Tentativas: {}/{}'.format(num_tentativas, max_tentativas), 
    fg=cor_letra, bg=cor_fundo, font=font_style
    )

label_tentativas.grid(
    row=num_linhas, columnspan=num_colunas, padx=10, pady=10
    )

janela.mainloop()