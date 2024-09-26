import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot


def main():
    # Init game
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        # Delta time
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        for thing in updatable:
            thing.update(dt)

            if isinstance(thing, Asteroid) and thing.is_colliding(player):
                print("Game over!")
                exit()

        # Render
        window.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(window)

        pygame.display.flip()


if __name__ == "__main__":
    main()
