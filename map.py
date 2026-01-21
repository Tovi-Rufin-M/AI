import pygame
import random
import sys

# ===== MAZE SETTINGS =====
WIDTH = 20
HEIGHT = 20
CELL_SIZE = 30

SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

# Colors
RED = (200, 0, 0)
GREEN = (0, 180, 0)
BLACK = (0, 0, 0)

# Initialize maze with walls
maze = [[1 for _ in range(WIDTH)] for _ in range(HEIGHT)]

DIRS = [(0, -2), (0, 2), (-2, 0), (2, 0)]

def in_bounds(x, y):
    return 0 < x < WIDTH - 1 and 0 < y < HEIGHT - 1

def carve(x, y):
    maze[y][x] = 0
    random.shuffle(DIRS)

    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and maze[ny][nx] == 1:
            maze[y + dy // 2][x + dx // 2] = 0
            carve(nx, ny)

# Generate maze
carve(1, 1)
maze[0][1] = 0
maze[HEIGHT - 1][WIDTH - 2] = 0

# ===== PYGAME SETUP =====
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Visualization")

clock = pygame.time.Clock()

def draw_maze():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = GREEN if maze[y][x] == 0 else RED
            pygame.draw.rect(
                screen,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

# ===== MAIN LOOP =====
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_maze()
    pygame.display.flip()

pygame.quit()
sys.exit()
