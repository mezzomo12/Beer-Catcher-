import pygame
from recursos.funcoes import *
pygame.init()

tamanho = 1000, 700
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Bullet Hell!")
relogio = pygame.time.Clock()
personagem = pygame.image.load("assets/personagem.png")
fundoJogo = pygame.image.load("assets/background.png")
cerveja = pygame.image.load("assets/cerveja.png")

posicaoXPersonagem = 500
posicaoYPersonagem = 350
movimentoXPersonagem = 0
movimentoYPersonagem = 0
velocidadePersonagem = 5

# Get character dimensions
larguraPersonagem, alturaPersonagem = personagem.get_size()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimentoXPersonagem = velocidadePersonagem
            if evento.key == pygame.K_LEFT:
                movimentoXPersonagem = -velocidadePersonagem
            if evento.key == pygame.K_UP:
                movimentoYPersonagem = -velocidadePersonagem
            if evento.key == pygame.K_DOWN:
                movimentoYPersonagem = velocidadePersonagem
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                movimentoXPersonagem = 0
            if evento.key in [pygame.K_UP, pygame.K_DOWN]:
                movimentoYPersonagem = 0

    # Update character position
    posicaoXPersonagem += movimentoXPersonagem
    posicaoYPersonagem += movimentoYPersonagem

    # Handle boundaries
    if posicaoXPersonagem < 0:
        posicaoXPersonagem = 0
    if posicaoXPersonagem > tamanho[0] - larguraPersonagem:
        posicaoXPersonagem = tamanho[0] - larguraPersonagem
    if posicaoYPersonagem < 0:
        posicaoYPersonagem = 0
    if posicaoYPersonagem > tamanho[1] - alturaPersonagem:
        posicaoYPersonagem = tamanho[1] - alturaPersonagem

    # Draw everything
    tela.blit(fundoJogo, (0, 0))
    tela.blit(personagem, (posicaoXPersonagem, posicaoYPersonagem))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()