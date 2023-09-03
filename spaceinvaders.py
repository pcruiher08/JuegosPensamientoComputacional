import pygame
import sys
import random

# constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 0, 0)
BULLET_COLOR = (0, 0, 255)

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 50
BULLET_WIDTH, BULLET_HEIGHT = 10, 30

PLAYER_SPEED = 5
ENEMY_SPEED = 2
BULLET_SPEED = 5

ENEMY_ROWS = 3
ENEMY_COLS = 10

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()


player_rect = pygame.Rect(WIDTH // 2 - PLAYER_WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

# balas
bullets = []

# bloques
enemies = []
for row in range(ENEMY_ROWS):
    for col in range(ENEMY_COLS):
        enemy_rect = pygame.Rect(
            col * (ENEMY_WIDTH + 10) + 50,
            row * (ENEMY_HEIGHT + 10) + 50,
            ENEMY_WIDTH,
            ENEMY_HEIGHT
        )
        enemies.append(enemy_rect)


score = 0
font = pygame.font.Font(None, 36)


game_over = False

# ciclo de juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = pygame.Rect(
                    player_rect.centerx - BULLET_WIDTH // 2,
                    player_rect.top - BULLET_HEIGHT,
                    BULLET_WIDTH,
                    BULLET_HEIGHT
                )
                bullets.append(bullet_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

    # mover balas
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

    # mover bloques
    for enemy in enemies:
        enemy.x += ENEMY_SPEED
        if enemy.right >= WIDTH or enemy.left <= 0:
            ENEMY_SPEED *= -1
            for e in enemies:
                e.y += 30

    # choques
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10

    # fin de juego?
    for enemy in enemies:
        if enemy.colliderect(player_rect):
            game_over = True

    # pantalla vacia
    screen.fill(BLACK)

    # dibujar jugador
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    # dibujar balas
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)

    # dibujar enemigos
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)

    # score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # actualizar juego
    pygame.display.flip()

    # fps
    clock.tick(60)

# pantalla fin de juego
screen.fill(BLACK)
game_over_text = font.render("Perdiste", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()


pygame.time.delay(2000)
pygame.quit()
