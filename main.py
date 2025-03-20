# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =     pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    
    player = Player(SCREEN_WIDTH * 1 / 3,SCREEN_HEIGHT / 2,1)
    player2 = Player(SCREEN_WIDTH * 2 / 3,SCREEN_HEIGHT / 2,2,"red")
    asteroidField = AsteroidField()
    while True :
        screen.fill("black")

        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!\nPlayer 1 Died")
                sys.exit()
            if asteroid.check_collision(player2):
                print("Game over!\nPlayer 2 Died")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split(shot)
                    shot.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        text = my_font.render(f"Score 1 : {player.score}",True,(255,255,255))
        screen.blit(text,(0,0))
        text = my_font.render(f"Score 2 : {player2.score}",True,(255,255,255))
        screen.blit(text,(SCREEN_WIDTH-200,0))
        pygame.display.flip()
        dt = clock.tick(FPS)/1000


if __name__ == "__main__":
    main()