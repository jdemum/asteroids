import pygame
from constants import *
from player import Player  # Import the Player class directly 
from CircleShape import CircleShape                    
from asteroidfield import AsteroidField
from asteroid import Asteroid
from sys import exit

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # Set containers before creating instances
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    # Now create the player instance with a different name
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the main() function and close the program
        # Draw screen and fill color        
        screen.fill((0, 0, 0))
        # Control player movement
        updatable.update(dt)
        # Check for collision
        for asteroid in asteroids:
           if asteroid.collision(player_instance):
               print("Game Over!")
               sys.exit()

        # Draw player on the screen
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        # Only call clock.tick once - this line both limits the framerate and returns the time passed
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    print("About to start main")
    main()
    print("Main has returned")