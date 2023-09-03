import pygame
import sys
import random

# constantes
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
MOLE_COLOR = (255, 0, 0)
MOLE_SIZE = 50
GAME_TIME = 20  # segundos

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whackamole")
clock = pygame.time.Clock()

# variables
mole_x, mole_y = 0, 0
score = 0
time_remaining = GAME_TIME * 1000  # millisegundos
font = pygame.font.Font(None, 36)

# ciclo de juego
while time_remaining > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mole_x <= event.pos[0] <= mole_x + MOLE_SIZE and mole_y <= event.pos[1] <= mole_y + MOLE_SIZE:
                score += 1
                mole_x, mole_y = random.randint(0, WIDTH - MOLE_SIZE), random.randint(0, HEIGHT - MOLE_SIZE)

    screen.fill(BG_COLOR)
    
    # dibujar el mole
    if time_remaining > 0:
        pygame.draw.rect(screen, MOLE_COLOR, (mole_x, mole_y, MOLE_SIZE, MOLE_SIZE))
    
    # mostrar score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    time_text = font.render(f"Tiempo: {time_remaining // 1000}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (WIDTH - 120, 10))
    
    pygame.display.update()
    clock.tick(60)
    time_remaining -= 1000 / 60  # reducir el tiempo un segundo cada tick

# pantalla fin de juego
game_over_text = font.render("Fin del juego!", True, (255, 255, 255))
final_score_text = font.render(f"Score final: {score}", True, (255, 255, 255))
screen.fill(BG_COLOR)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 50))
pygame.display.update()

# esperar 3 segundos antes de salir del juego
pygame.time.wait(3000)
pygame.quit()
sys.exit()
