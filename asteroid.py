import pygame

from circle import Circle


class Asteroid(Circle):
    ASTEROID_MIN_RADIUS = 20
    ASTEROID_KINDS = 3
    ASTEROID_SPAWN_RATE = 0.8  # seconds
    ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, window):
        white = (255, 255, 255)
        pygame.draw.circle(window, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
