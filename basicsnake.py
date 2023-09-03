import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Initialize game state
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = random.choice([UP, DOWN, LEFT, RIGHT])
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Functions
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, WHITE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def move_snake(snake, direction, food):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    if new_head == food:
        snake.insert(0, new_head)
        return True
    else:
        snake.insert(0, new_head)
        snake.pop()
        return False

def check_collision(snake):
    head = snake[0]
    if head in snake[1:]:
        return True
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        return True
    return False

def generate_food(snake):
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food not in snake:
            return food

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT

    food_eaten = move_snake(snake, direction, food)
    if food_eaten:
        food = generate_food(snake)

    if check_collision(snake):
        running = False

    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()