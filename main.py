import pygame
import random
from recursos.funcoes import *
import tkinter as tk
from tkinter import messagebox
from recursos.funcoes import inicializarBancoDeDados
from recursos.funcoes import escreverDados
import json

pygame.init()

tamanho = 1000, 700
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Beer Catcher!")
fonte = pygame.font.SysFont("arial", 36)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)

button_width, button_height = 200, 50
play_button_rect = pygame.Rect((tamanho[0] // 2 - button_width // 2, tamanho[1] // 2 - 100), (button_width, button_height))
quit_button_rect = pygame.Rect((tamanho[0] // 2 - button_width // 2, tamanho[1] // 2), (button_width, button_height))

input_box = pygame.Rect(tamanho[0] // 2 - 150, tamanho[1] // 2 + 100, 300, 50)
active = False
player_name = ""

def draw_menu():
    tela.fill(PRETO)
    title_text = fonte.render("Beer Catcher!", True, BRANCO)
    tela.blit(title_text, (tamanho[0] // 2 - title_text.get_width() // 2, 100))

    pygame.draw.rect(tela, CINZA, play_button_rect)
    play_text = fonte.render("Play", True, PRETO)
    tela.blit(play_text, (play_button_rect.x + button_width // 2 - play_text.get_width() // 2, play_button_rect.y + button_height // 2 - play_text.get_height() // 2))

    pygame.draw.rect(tela, CINZA, quit_button_rect)
    quit_text = fonte.render("Quit", True, PRETO)
    tela.blit(quit_text, (quit_button_rect.x + button_width // 2 - quit_text.get_width() // 2, quit_button_rect.y + button_height // 2 - quit_text.get_height() // 2))

    pygame.display.flip()

def draw_name_input():
    tela.fill(PRETO)
    prompt_text = fonte.render("Enter your name:", True, BRANCO)
    tela.blit(prompt_text, (tamanho[0] // 2 - prompt_text.get_width() // 2, tamanho[1] // 2 - 50))

    pygame.draw.rect(tela, BRANCO, input_box, 2)
    name_text = fonte.render(player_name, True, BRANCO)
    tela.blit(name_text, (input_box.x + 10, input_box.y + 10))

    pygame.display.flip()

def draw_welcome_screen(player_name):
    tela.fill(PRETO)
    welcome_text = fonte.render(f"Bem-vindo(a) {player_name}!", True, BRANCO)
    instructions_line1 = fonte.render(
        "Esse jogo é do estilo food drop.",
        True,
        BRANCO,
    )
    instructions_line2 = fonte.render(
        "Mova-se para os lados com as setas do teclado",
        True,
        BRANCO,
    )
    instructions_line3 = fonte.render(
        "e pegue o máximo de cervejas que conseguir, mas evite os repolhos.",
        True,
        BRANCO,
    )

    tela.blit(welcome_text, (tamanho[0] // 2 - welcome_text.get_width() // 2, tamanho[1] // 2 - 200))
    tela.blit(instructions_line1, (tamanho[0] // 2 - instructions_line1.get_width() // 2, tamanho[1] // 2 - 100))
    tela.blit(instructions_line2, (tamanho[0] // 2 - instructions_line2.get_width() // 2, tamanho[1] // 2 - 50))
    tela.blit(instructions_line3, (tamanho[0] // 2 - instructions_line3.get_width() // 2, tamanho[1] // 2))

    play_button_rect = pygame.Rect((tamanho[0] // 2 - button_width // 2, tamanho[1] // 2 + 100), (button_width, button_height))
    pygame.draw.rect(tela, CINZA, play_button_rect)
    play_text = fonte.render("Play", True, PRETO)
    tela.blit(play_text, (play_button_rect.x + button_width // 2 - play_text.get_width() // 2, play_button_rect.y + button_height // 2 - play_text.get_height() // 2))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    return  # Exit the welcome screen and start the game

menu_running = True
while menu_running:
    draw_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                while True:
                    draw_name_input()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN and player_name.strip():
                                menu_running = False
                                draw_welcome_screen(player_name)  # Show welcome screen
                                break
                            elif event.key == pygame.K_BACKSPACE:
                                player_name = player_name[:-1]
                            else:
                                player_name += event.unicode
                    if not menu_running:
                        break
            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

import pygame
import random
from recursos.funcoes import *
import tkinter as tk
from tkinter import messagebox
from recursos.funcoes import inicializarBancoDeDados
from recursos.funcoes import escreverDados
import json

pygame.init()

tamanho = 1000, 700
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Beer Catcher!")
relogio = pygame.time.Clock()

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
pygame.mixer.music.play(-1)


posicaoXPersonagem = 500
posicaoYPersonagem = tamanho[1] - 180
movimentoXPersonagem = 0
velocidadePersonagem = 10

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

def show_score_log():
    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []

    root = tk.Tk()
    root.title("Tela da Morte")
    root.geometry("400x300")

    title_label = tk.Label(root, text="Log das Partidas", font=("Arial", 16))
    title_label.pack(pady=10)

    text_widget = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
    text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    for score_entry in scores:
        name = score_entry.get("name", "Unknown")
        score = score_entry.get("score", 0)
        date = score_entry.get("date", "Unknown Date")
        text_widget.insert(tk.END, f"Pontos: {score} na data: {date} - Nickname: {name}\n")

    text_widget.config(state=tk.DISABLED)

    root.mainloop()

def save_score(name, score):
    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []

    from datetime import datetime
    current_date = datetime.now().strftime("%d/%m/%Y")

    scores.append({"name": name, "score": score, "date": current_date})

    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)

paused = False

def draw_pause_screen():
    tela.fill(PRETO)
    pause_text = fonte.render("Game Paused", True, BRANCO)
    tela.blit(pause_text, (tamanho[0] // 2 - pause_text.get_width() // 2, tamanho[1] // 2 - 100))

    resume_button_rect = pygame.Rect((tamanho[0] // 2 - button_width // 2, tamanho[1] // 2), (button_width, button_height))
    pygame.draw.rect(tela, CINZA, resume_button_rect)
    resume_text = fonte.render("Resume", True, PRETO)
    tela.blit(resume_text, (resume_button_rect.x + button_width // 2 - resume_text.get_width() // 2, resume_button_rect.y + button_height // 2 - resume_text.get_height() // 2))

    pygame.display.flip()
    return resume_button_rect

def draw_death_screen():
    tela.fill(PRETO)
    death_screen = pygame.image.load("assets/tela_morte.png")
    death_screen = pygame.transform.scale(death_screen, tamanho)
    tela.blit(death_screen, (0, 0))

    play_again_button_rect = pygame.Rect((tamanho[0] // 2 - button_width // 2, tamanho[1] // 2 - 100), (button_width, button_height))
    pygame.draw.rect(tela, CINZA, play_again_button_rect)
    play_again_text = fonte.render("Play Again", True, PRETO)
    tela.blit(play_again_text, (play_again_button_rect.x + button_width // 2 - play_again_text.get_width() // 2, play_again_button_rect.y + button_height // 2 - play_again_text.get_height() // 2))

    quit_button_rect = pygame.Rect((tamanho[0] // 2 - button_width // 2, tamanho[1] // 2), (button_width, button_height))
    pygame.draw.rect(tela, CINZA, quit_button_rect)
    quit_text = fonte.render("Quit", True, PRETO)
    tela.blit(quit_text, (quit_button_rect.x + button_width // 2 - quit_text.get_width() // 2, quit_button_rect.y + button_height // 2 - quit_text.get_height() // 2))

    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []

    last_matches = scores[-5:]
    y_offset = tamanho[1] // 2 + 100
    for match in last_matches:
        name = match.get("name", "Unknown")
        score = match.get("score", 0)
        date = match.get("date", "Unknown Date")
        match_text = fonte.render(f"{date} - {name}: {score} pontos", True, BRANCO)
        tela.blit(match_text, (tamanho[0] // 2 - match_text.get_width() // 2, y_offset))
        y_offset += 40 

    pygame.display.flip()
    return play_again_button_rect, quit_button_rect

def reset_game():
    global pontos, posicaoXPersonagem, posicaoYPersonagem, movimentoXPersonagem, velocidadePersonagem, cervejas, repolhos

    pontos = 0
    posicaoXPersonagem = 500
    posicaoYPersonagem = tamanho[1] - 180
    movimentoXPersonagem = 0
    velocidadePersonagem = 10

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

    pygame.mixer.music.play(-1)

barril = pygame.image.load("assets/barril.png")
barril_original = pygame.transform.scale(barril, (100, 100))  # Initial size
barril_rect = barril_original.get_rect()
barril_rect.bottomright = (tamanho[0] - 20, tamanho[1] - 20)

pulse_scale = 100
pulse_direction = 1
pulse_speed = 1

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                paused = not paused
            if not paused:
                if evento.key == pygame.K_RIGHT:
                    movimentoXPersonagem = velocidadePersonagem
                    personagem = personagem_original
                if evento.key == pygame.K_LEFT:
                    movimentoXPersonagem = -velocidadePersonagem
                    personagem = pygame.transform.flip(personagem_original, True, False)
            if paused and evento.type == pygame.MOUSEBUTTONDOWN:
                if resume_button_rect.collidepoint(evento.pos):
                    paused = False
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                movimentoXPersonagem = 0

    if paused:
        resume_button_rect = draw_pause_screen()
        continue

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
            save_score(player_name, pontos)
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Game Over", f"Game Over! {player_name}, your score is {pontos}.")
            root.destroy()

            while True:
                play_again_button_rect, quit_button_rect = draw_death_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_again_button_rect.collidepoint(event.pos):
                            reset_game()  # Reset the game
                            break
                        elif quit_button_rect.collidepoint(event.pos):
                            pygame.quit()
                            exit()
                else:
                    continue
                break

    pulse_scale += pulse_direction * pulse_speed
    if pulse_scale >= 120 or pulse_scale <= 80:
        pulse_direction *= -1
    barril_scaled = pygame.transform.scale(barril, (pulse_scale, pulse_scale))
    barril_rect = barril_scaled.get_rect()
    barril_rect.bottomright = (tamanho[0] - 20, tamanho[1] - 20)

    tela.blit(fundoJogo, (0, 0))
    tela.blit(personagem, (posicaoXPersonagem, posicaoYPersonagem))

    for x, y in cervejas:
        tela.blit(cerveja, (x, y))

    for x, y in repolhos:
        tela.blit(repolho, (x, y))

    tela.blit(barril_scaled, barril_rect)

    textoPontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(textoPontos, (10, 10))

    fonteMenor = pygame.font.SysFont("arial", 20)  # Smaller font for instructions
    textoPause = fonteMenor.render("Press space to pause the game", True, (255, 255, 255))
    tela.blit(textoPause, (textoPontos.get_width() + 20, 15))  # Position next to the score

    pygame.display.flip()
    relogio.tick(60)