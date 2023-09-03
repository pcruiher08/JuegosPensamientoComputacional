import pygame
import sys
import random

# constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ahorcado")
clock = pygame.time.Clock()

# fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# palabras
words = ['MONTERREY', 'PROGRAMACION', 'JUEGOS', 'MEMORIA', 'TECLADO']
current_word = random.choice(words)
guessed_word = ['_' for _ in current_word]

# variables de juego
attempts = 0
max_attempts = 6  # pasos para terminar de dibujar al mono
game_over = False
won = False

# ciclo de juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not won and attempts < max_attempts:
            if event.type == pygame.KEYDOWN and event.unicode in ALPHABET:
                letter = event.unicode
                if letter in current_word:
                    for i, char in enumerate(current_word):
                        if char == letter:
                            guessed_word[i] = letter
                else:
                    attempts += 1

            # palabra completa
            if ''.join(guessed_word) == current_word:
                won = True


    screen.fill(WHITE)

    # palabra
    word_text = font.render(' '.join(guessed_word), True, BLACK)
    screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, 400))

    # mono
    if attempts < max_attempts:
        pygame.draw.line(screen, BLACK, (300, 100), (300, 30), 5)  # estructural
        pygame.draw.line(screen, BLACK, (250, 100), (350, 100), 5)
        pygame.draw.line(screen, BLACK, (300, 30), (500, 30), 5)  #  barra horizontal
        pygame.draw.line(screen, BLACK, (500, 30), (500, 400), 5)  # barra verical
        pygame.draw.circle(screen, BLACK, (500, 150), 30, 5)  # cabeza

        if attempts > 0:
            pygame.draw.line(screen, BLACK, (500, 180), (500, 300), 5)  # cuerpo
        if attempts > 1:
            pygame.draw.line(screen, BLACK, (500, 200), (470, 240), 5)  # brazo izquierdo
        if attempts > 2:
            pygame.draw.line(screen, BLACK, (500, 200), (530, 240), 5)  # brazo derecho
        if attempts > 3:
            pygame.draw.line(screen, BLACK, (500, 300), (470, 340), 5)  # pierna izquierda
        if attempts > 4:
            pygame.draw.line(screen, BLACK, (500, 300), (530, 340), 5)  # pierna derecha
    else:
        game_over = True

    # valida gane o pierde
    if won:
        result_text = font.render("You Win!", True, BLACK)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 200))
    elif game_over:
        result_text = font.render("Game Over", True, BLACK)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 200))
        word_text = font.render(current_word, True, BLACK)
        screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, 300))

    pygame.display.flip()
    # fps
    clock.tick(60)
