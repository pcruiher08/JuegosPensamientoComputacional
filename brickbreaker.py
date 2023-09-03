import pygame
import sys
import random

# constantes del juego
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
PADDLE_COLOR = (0, 255, 0)
BALL_COLOR = (255, 255, 255)
BRICK_COLOR = (255, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 10
BALL_SIZE = 20
BRICK_WIDTH, BRICK_HEIGHT = 80, 20
BRICK_ROWS = 5
BRICK_COLS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# establecer canvas de juego
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick breaker")
clock = pygame.time.Clock()

# variables iniciales
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx = BALL_SPEED_X
ball_dy = -BALL_SPEED_Y

# crear ladrillos
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + 5) + 30
        brick_y = row * (BRICK_HEIGHT + 5) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

# dibujar base
def draw_paddle(x, y):
    pygame.draw.rect(screen, PADDLE_COLOR, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

# dibujar bola
def draw_ball(x, y):
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_SIZE)

# dibujar ladrillos
def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

# ciclo de juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 7
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += 7

    # mover bola
    ball_x += ball_dx
    ball_y += ball_dy

    # bola choca con paredes
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    # bola choca con base
    if (
        paddle_x < ball_x < paddle_x + PADDLE_WIDTH and
        paddle_y < ball_y < paddle_y + PADDLE_HEIGHT
    ):
        ball_dy *= -1

    # bola choca con los ladrillos
    for brick in bricks:
        if brick.colliderect(pygame.Rect(ball_x - BALL_SIZE, ball_y - BALL_SIZE, BALL_SIZE * 2, BALL_SIZE * 2)):
            ball_dy *= -1
            bricks.remove(brick)

    screen.fill(BG_COLOR)
    draw_paddle(paddle_x, paddle_y)
    draw_ball(ball_x, ball_y)
    draw_bricks()

    pygame.display.update()
    clock.tick(60)
