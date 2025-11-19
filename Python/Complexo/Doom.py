import pygame
import math
import sys

# Inicialização
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Doom - Raycasting")
clock = pygame.time.Clock()

# Cores
BLACK = (0, 0, 0)

# Mapa (8x8): 1 = parede, 0 = espaço
world_map = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],
]

# Jogador
px, py = 3.5, 3.5  # posição inicial
pa = 0.0001        # ângulo inicial (evita divisão por zero)
FOV = math.pi / 3  # 60 graus
DEPTH = 16
SPEED = 0.05

def cast_rays():
    for x in range(0, WIDTH):
        ray_angle = (pa - FOV / 2.0) + (x / WIDTH) * FOV
        distance_to_wall = 0
        hit_wall = False

        eye_x = math.cos(ray_angle)
        eye_y = math.sin(ray_angle)

        while not hit_wall and distance_to_wall < DEPTH:
            distance_to_wall += 0.05
            test_x = int(px + eye_x * distance_to_wall)
            test_y = int(py + eye_y * distance_to_wall)

            if test_x < 0 or test_x >= 8 or test_y < 0 or test_y >= 8:
                hit_wall = True
                distance_to_wall = DEPTH
            elif world_map[test_y][test_x] == 1:
                hit_wall = True

        # Evitar divisão por zero
        if distance_to_wall == 0:
            distance_to_wall = 0.1

        # Calcular altura da parede
        wall_height = int(HEIGHT / distance_to_wall)
        wall_height = min(wall_height, HEIGHT)

        start_y = int((HEIGHT - wall_height) / 2)
        end_y = start_y + wall_height

        # Cor com sombreamento
        shade = 255 - min(int(distance_to_wall * 20), 255)
        color = (shade, shade, shade)

        pygame.draw.line(screen, color, (x, start_y), (x, end_y))

def move_player():
    global px, py, pa
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pa -= 0.05
    if keys[pygame.K_RIGHT]:
        pa += 0.05
    if keys[pygame.K_UP]:
        nx = px + math.cos(pa) * SPEED
        ny = py + math.sin(pa) * SPEED
        if world_map[int(ny)][int(nx)] == 0:
            px, py = nx, ny
    if keys[pygame.K_DOWN]:
        nx = px - math.cos(pa) * SPEED
        ny = py - math.sin(pa) * SPEED
        if world_map[int(ny)][int(nx)] == 0:
            px, py = nx, ny

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    move_player()
    cast_rays()
    pygame.display.flip()
    clock.tick(60)
