import pygame
import random
from recursos.funcoes import *
pygame.init()

tamanho = 1000, 700
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Bullet Hell!")
relogio = pygame.time.Clock()

# Load and scale images
personagem_original = pygame.image.load("assets/personagem.png")
personagem_original = pygame.transform.scale(personagem_original, (80, 70))  # Scale character to 80x70 pixels
personagem = personagem_original  # Default orientation
fundoJogo = pygame.image.load("assets/background.png")
cerveja = pygame.image.load("assets/cerveja.png")
cerveja = pygame.transform.scale(cerveja, (30, 30))  # Scale cerveja to 30x30 pixels

posicaoXPersonagem = 500
posicaoYPersonagem = 350
movimentoXPersonagem = 0
movimentoYPersonagem = 0
velocidadePersonagem = 5

# Get dimensions
larguraPersonagem, alturaPersonagem = personagem.get_size()
larguraCerveja, alturaCerveja = cerveja.get_size()

# Initial cerveja position
posicaoXCerveja = random.randint(0, tamanho[0] - larguraCerveja)
posicaoYCerveja = random.randint(0, tamanho[1] - alturaCerveja)

# Points system
pontos = 0
fonte = pygame.font.SysFont("arial", 36)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimentoXPersonagem = velocidadePersonagem
                personagem = personagem_original  # Face right
            if evento.key == pygame.K_LEFT:
                movimentoXPersonagem = -velocidadePersonagem
                personagem = pygame.transform.flip(personagem_original, True, False)  # Flip horizontally
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

    # Check collision with cerveja
    if (
        posicaoXPersonagem < posicaoXCerveja + larguraCerveja and
        posicaoXPersonagem + larguraPersonagem > posicaoXCerveja and
        posicaoYPersonagem < posicaoYCerveja + alturaCerveja and
        posicaoYPersonagem + alturaPersonagem > posicaoYCerveja
    ):
        pontos += 1
        posicaoXCerveja = random.randint(0, tamanho[0] - larguraCerveja)
        posicaoYCerveja = random.randint(0, tamanho[1] - alturaCerveja)

    # Draw everything
    tela.blit(fundoJogo, (0, 0))
    tela.blit(personagem, (posicaoXPersonagem, posicaoYPersonagem))
    tela.blit(cerveja, (posicaoXCerveja, posicaoYCerveja))

    # Display points
    textoPontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(textoPontos, (10, 10))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()