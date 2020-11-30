######
# Step 2: include laser beam that is activated when user presses the Space bar

import pygame
from my_game import Ship, Asteroid
from random import randint
import sys

# Initialize game state
ship = Ship()
asteroid_count = 10
asteroids = [Asteroid() for _ in range(0, asteroid_count)]

for asteroid in asteroids:
    asteroid.x = randint(-9, 9)
    asteroid.y = randint(-9, 9)

# colors and settings

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

width, height = 400, 400

def to_pixels(x, y):
    return (width / 2 + width * x / 20, height / 2 - height * y / 20)

def draw_poly(screen, polygon_model, color=GREEN):
    pixel_points = [to_pixels(x, y) for x, y in polygon_model.transformed()]
    pygame.draw.aalines(screen, color, True, pixel_points, 10)

# added in section 7.1.6
def draw_segment(screen, v1, v2, color=RED):
    pygame.draw.aaline(screen, color, to_pixels(*v1), to_pixels(*v2), 10)

def main():
    pygame.display.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Asteroids')

    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # added in section 7.1.6
        laser = ship.laser_segment()            

        screen.fill(BLACK)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)

        draw_poly(screen, ship)
        for asteroid in asteroids:
            draw_poly(screen, asteroid, color=GREEN)
        
        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()