import random 
import pygame


pygame.init()
pygame.display.set_caption('Cobrona do italo em python')
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores rgb
verde = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
verde_escuro = (0, 100, 0)
roxo = (128, 0, 128)

# parametros da cobra
tamanho_quadrado = 20
velocidade_cobra = 15

def gerador_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0 
    return comida_x, comida_y 

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixeis):
    for pixel in pixeis:
        pygame.draw.rect(tela, roxo, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    font = pygame.font.SysFont("Arial", 35)
    texto = font.render(f'Pontos: {pontuacao}', True, branca)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    if tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = - tamanho_quadrado
    if tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    if tecla == pygame.K_LEFT:
        velocidade_x = - tamanho_quadrado
        velocidade_y = 0

    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_do = False

    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixeis = []

    comida_x, comida_y = gerador_comida()
    

    while not fim_do:
        tela.fill(verde_escuro)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_do = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # Atualizar a posição da cobra 
        if x< 0 or x >= largura or y < 0 or y >= altura:
            fim_do = True

        x += velocidade_x
        y += velocidade_y

        
        # Desenhar_comida 
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # Desenhar_cobra
        pixeis.append((x, y))
        if len(pixeis) > tamanho_cobra:
            del pixeis[0]

        # cobra bateu no proprio corpo
        for pixel in pixeis[:-1]:
            if pixel == (x, y):
                fim_do = True
        
        desenhar_cobra (tamanho_quadrado, pixeis)
        desenhar_pontuacao(tamanho_cobra - 1)

        # Desenhar_pontos

        # Atualização da tela
        pygame.display.update()

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerador_comida()

        relogio.tick(velocidade_cobra)

rodar_jogo()