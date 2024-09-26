import pygame

from circle import Circle


class Shot(Circle):
    SHOT_RADIUS = 5

    def __init__(self, x, y, velocity):
        super().__init__(x, y, Shot.SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, window):
        white = (255, 255, 255)
        pygame.draw.circle(window, white, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
