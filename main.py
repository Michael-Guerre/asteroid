# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    while True :
        screen.fill("black")

        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_Collision(player):
                print("Game over!")
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        pygame.display.flip()
        dt = clock.tick(FPS)/1000


if __name__ == "__main__":
    main()