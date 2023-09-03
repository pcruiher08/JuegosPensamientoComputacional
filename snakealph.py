import pygame
import sys
import random

# constantes
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# tuplas de direcciones
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alphabet Snake Game")
clock = pygame.time.Clock()

# estado inicial del juego
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = random.choice([UP, DOWN, LEFT, RIGHT])
foods = [chr(65)]  # primer letra es A

def random_food_position(snake, food_positions):
    while True:
        position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if position not in snake and position not in food_positions:
            return position
food_positions = [random_food_position(snake, [])]

food_positions = [random_food_position(snake, food_positions)]

# funciones
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food, position):
    font = pygame.font.Font(None, 36)
    text = font.render(food, True, WHITE)
    screen.blit(text, (position[0] * GRID_SIZE + 5, position[1] * GRID_SIZE + 5))

def move_snake(snake, direction):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    if new_head in food_positions:
        food_index = food_positions.index(new_head)
        if food_index == len(foods) - 1:
            next_letter = chr(ord(foods[-1]) + 1)
            if next_letter <= 'Z':
                foods.append(next_letter)
                food_positions.append(random_food_position(snake, food_positions))
            else:
                # si se come la z, gana
                print("You Win!")
                pygame.quit()
                sys.exit()
        else:
            foods.pop(food_index)
            food_positions.pop(food_index)
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

# ciclo de juego
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

    food_eaten = move_snake(snake, direction)

    if check_collision(snake):
        print("Fin del juego!")
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    draw_snake(snake)
    for food, position in zip(foods, food_positions):
        draw_food(food, position)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
