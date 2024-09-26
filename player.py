import pygame

from circle import Circle
from shot import Shot


class Player(Circle):
    PLAYER_SHOOT_SPEED = 500
    PLAYER_SHOOT_COOLDOWN = 0.3

    def __init__(self, x, y):
        super().__init__(x, y, 20)
        self.rotation = 0
        self.turn_speed = 300
        self.move_speed = 200
        self.__shot_timer = 0

    def triangle(self):
        # Negative is up on the y-axis, positive is down
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90)

        a = self.position + forward * self.radius

        # Base of the triangle
        base = self.position - forward * self.radius
        scale = 1.5

        # Left and right points at the base of the triangle
        b = base - right * self.radius / scale  # Move left
        c = base + right * self.radius / scale  # Move right

        return [a, b, c]

    def shoot(self):
        if self.__shot_timer <= 0:
            velocity = pygame.Vector2(0, -1).rotate(self.rotation)
            Shot(self.position.x, self.position.y, velocity * Player.PLAYER_SHOOT_SPEED)
            self.__shot_timer = Player.PLAYER_SHOOT_COOLDOWN

    def draw(self, window):
        pygame.draw.polygon(window, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += dt * self.turn_speed

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * dt * self.move_speed

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.__shot_timer -= dt
