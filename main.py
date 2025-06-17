import pygame
import random
from recursos.funcoes import *

pygame.init()

# Screen setup
tamanho = 1000, 700
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Bullet Hell!")
relogio = pygame.time.Clock()

# Load assets
personagem_original = pygame.image.load("assets/personagem.png")
personagem_original = pygame.transform.scale(personagem_original, (180, 170))
personagem = personagem_original
fundoJogo = pygame.image.load("assets/background.png")
cerveja = pygame.image.load("assets/cerveja.png")
cerveja = pygame.transform.scale(cerveja, (80, 80))
repolho = pygame.image.load("assets/repolho.png")
repolho = pygame.transform.scale(repolho, (80, 80))
som_pontos = pygame.mixer.Sound("assets/ponto.wav")
som_pontos.set_volume(0.2)
pygame.mixer.music.load("assets/musica.mp3")
pygame.mixer.music.play(-1)  # Loop background music

# Load play button
botao_jogar = pygame.image.load("assets/botao_jogar.png")
botao_jogar = pygame.transform.scale(botao_jogar, (300, 100))  # Scale button

# Character setup
posicaoXPersonagem = 500
posicaoYPersonagem = tamanho[1] - 180
movimentoXPersonagem = 0
velocidadePersonagem = 10

# Object setup
larguraPersonagem, alturaPersonagem = personagem.get_size()
larguraCerveja, alturaCerveja = cerveja.get_size()
larguraRepolho, alturaRepolho = repolho.get_size()

num_cervejas = 7
num_repolhos = 4

cervejas = []
for _ in range(num_cervejas):
    x = random.randint(0, tamanho[0] - larguraCerveja)
    y = random.randint(-500, -80)
    cervejas.append([x, y])

repolhos = []
for _ in range(num_repolhos):
    x = random.randint(0, tamanho[0] - larguraRepolho)
    y = random.randint(-500, -80)
    repolhos.append([x, y])

velocidadeCerveja = 3
velocidadeRepolho = 4

pontos = 0
fonte = pygame.font.SysFont("arial", 36)

# Function to display the menu
def menu():
    while True:
        tela.fill((0, 0, 0))  # Black background
        tela.blit(botao_jogar, (tamanho[0] // 2 - 150, tamanho[1] // 2 - 50))  # Center the button

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                botao_rect = botao_jogar.get_rect(topleft=(tamanho[0] // 2 - 150, tamanho[1] // 2 - 50))
                if botao_rect.collidepoint(mouse_pos):
                    return  # Start the game

        pygame.display.flip()
        relogio.tick(60)

# Show the menu
menu()

# Main game loop
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimentoXPersonagem = velocidadePersonagem
                personagem = personagem_original
            if evento.key == pygame.K_LEFT:
                movimentoXPersonagem = -velocidadePersonagem
                personagem = pygame.transform.flip(personagem_original, True, False)
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                movimentoXPersonagem = 0

    posicaoXPersonagem += movimentoXPersonagem

    if posicaoXPersonagem < 0:
        posicaoXPersonagem = 0
    if posicaoXPersonagem > tamanho[0] - larguraPersonagem:
        posicaoXPersonagem = tamanho[0] - larguraPersonagem

    for i in range(len(cervejas)):
        cervejas[i][1] += velocidadeCerveja
        if cervejas[i][1] > tamanho[1]:
            cervejas[i][1] = -alturaCerveja
            cervejas[i][0] = random.randint(0, tamanho[0] - larguraCerveja)

        if (
            posicaoXPersonagem < cervejas[i][0] + larguraCerveja and
            posicaoXPersonagem + larguraPersonagem > cervejas[i][0] and
            posicaoYPersonagem < cervejas[i][1] + alturaCerveja and
            posicaoYPersonagem + alturaPersonagem > cervejas[i][1]
        ):
            pontos += 1
            som_pontos.play()
            cervejas[i][1] = -alturaCerveja
            cervejas[i][0] = random.randint(0, tamanho[0] - larguraCerveja)

    for i in range(len(repolhos)):
        repolhos[i][1] += velocidadeRepolho
        if repolhos[i][1] > tamanho[1]:
            repolhos[i][1] = -alturaRepolho
            repolhos[i][0] = random.randint(0, tamanho[0] - larguraRepolho)

        if (
            posicaoXPersonagem < repolhos[i][0] + larguraRepolho and
            posicaoXPersonagem + larguraPersonagem > repolhos[i][0] and
            posicaoYPersonagem < repolhos[i][1] + alturaRepolho and
            posicaoYPersonagem + alturaPersonagem > repolhos[i][1]
        ):
            print("Game Over!")
            pygame.quit()
            exit()

    # Drawing
    tela.blit(fundoJogo, (0, 0))
    tela.blit(personagem, (posicaoXPersonagem, posicaoYPersonagem))

    # Draw all cervejas
    for x, y in cervejas:
        tela.blit(cerveja, (x, y))

    # Draw all repolhos
    for x, y in repolhos:
        tela.blit(repolho, (x, y))

    # Display points
    textoPontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(textoPontos, (10, 10))

    pygame.display.flip()
    relogio.tick(60)