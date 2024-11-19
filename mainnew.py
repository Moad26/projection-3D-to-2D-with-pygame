import pygame
import numpy as np
from rotation import rotate_vertices
from simpleprojection import projection_matrix

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100

circle_pos = [WIDTH/2, HEIGHT/2]

angle = 0

points = np.array([
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
])

points2d = np.empty((len(points), 2))

projection_matrix = projection_matrix()

def draw_line(i, j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]),
                    (points[j][0], points[j][1]))

clock = pygame.time.Clock()

while True:
    
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    screen.fill(WHITE)

    angle += 0.01
    
    i = 0
    for point in points:
        rotated_point = rotate_vertices(point, angle_x=angle,
                                         angle_y=angle, angle_z=angle)

        projected_point = rotated_point @ projection_matrix.T 
        x = projected_point[0] * scale + circle_pos[0]
        y = projected_point[1] * scale + circle_pos[1]

        points2d[i] = np.array([x, y])
        pygame.draw.circle(screen, BLACK, (x, y), 5)
        i += 1

    for p in range(4):
            draw_line(p, (p+1) % 4, points2d)
            draw_line(p+4, ((p+1) % 4) + 4, points2d)
            draw_line(p, (p+4), points2d)   
    pygame.display.update()