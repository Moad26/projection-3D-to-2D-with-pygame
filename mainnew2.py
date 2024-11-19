import pygame
import numpy as np
from perspective_projection import Projection
from perspectiverotation import Rotation

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

n, f, D, d = -200, -10, WIDTH, HEIGHT
aspect_ratio = WIDTH / HEIGHT
scale = 100

circle_pos = [WIDTH/2, HEIGHT/2]

angle = 0

points = np.array([
    [1, 1, -1],   # Front-top-right
    [1, -1, -1],  # Front-bottom-right
    [-1, -1, -1], # Front-bottom-left
    [-1, 1, -1],  # Front-top-left
    [1, 1, -3],   # Back-top-right
    [1, -1, -3],  # Back-bottom-right
    [-1, -1, -3], # Back-bottom-left
    [-1, 1, -3],  # Back-top-left
])

# Calculate the center of the cube
center = np.mean(points, axis=0)

points2d = np.empty((len(points), 2))

p1 = Projection(near=1, far=20, D=2 * aspect_ratio, d=2)
r1 = Rotation()


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
        rotated_point = r1.rotate_vertices(point, angle_x=0,
                                         angle_y=0, angle_z=angle, center_coor=center)

        projected_point = p1.GL_projection(rotated_point)
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