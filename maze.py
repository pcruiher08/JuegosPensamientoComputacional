import pygame
import sys
import random

# constantes
WIDTH, HEIGHT = 400, 400
BG_COLOR = (0, 0, 0)
WALL_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
GOAL_COLOR = (255, 0, 0)
PLAYER_SIZE = 20
WALL_SIZE = 30
GOAL_SIZE = 30
FPS = 60

# laberingo (0: vacio, 1: pared)
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

# validar posicion dentro del maze
def is_valid_position(x, y):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] == 0

# generar inicio y fin con random
def random_positions():
    while True:
        start_x, start_y = random.randint(1, len(maze[0]) - 2), random.randint(1, len(maze) - 2)
        goal_x, goal_y = random.randint(1, len(maze[0]) - 2), random.randint(1, len(maze) - 2)
        if is_valid_position(start_x, start_y) and is_valid_position(goal_x, goal_y):
            return start_x, start_y, goal_x, goal_y

START_X, START_Y, GOAL_X, GOAL_Y = random_positions()

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

# position de jugador
player_x, player_y = START_X, START_Y

# ciclo de juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and is_valid_position(player_x, player_y - 1):
        player_y -= 1
    if keys[pygame.K_DOWN] and is_valid_position(player_x, player_y + 1):
        player_y += 1
    if keys[pygame.K_LEFT] and is_valid_position(player_x - 1, player_y):
        player_x -= 1
    if keys[pygame.K_RIGHT] and is_valid_position(player_x + 1, player_y):
        player_x += 1

    # revisa si se llega al objetivo
    if player_x == GOAL_X and player_y == GOAL_Y:
        print("You Win!")
        START_X, START_Y, GOAL_X, GOAL_Y = random_positions()  # randomizar de nuevo
        player_x, player_y = START_X, START_Y  # Resetear jugador

    # dibujar laberinto
    screen.fill(BG_COLOR)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, WALL_COLOR, (x * WALL_SIZE, y * WALL_SIZE, WALL_SIZE, WALL_SIZE))
    pygame.draw.rect(screen, GOAL_COLOR, (GOAL_X * WALL_SIZE, GOAL_Y * WALL_SIZE, GOAL_SIZE, GOAL_SIZE))
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x * WALL_SIZE, player_y * WALL_SIZE, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.update()
    clock.tick(FPS)
