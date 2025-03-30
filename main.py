import pygame
from constants import *
from player import Player  # Import the Player class directly 
from CircleShape import CircleShape                    
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
from shot import Shot

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
    shots = pygame.sprite.Group()
    # Set containers before creating instances
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    # Now create the player instance with a different name
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the main() function and close the program
            
    
        keys = pygame.key.get_pressed()  # Check pressed keys
        if keys[pygame.K_SPACE]:         # Detect if spacebar is held
            player_instance.shoot()      # Call the shoot() method

        # Draw screen and fill color        
        screen.fill((0, 0, 0))
        # Control player movement
        updatable.update(dt)
        # Check for collision
        for asteroid in asteroids:
            distance = asteroid.position.distance_to(player_instance.position)
            sum_radii = asteroid.radius + player_instance.radius
            if asteroid.collision(player_instance):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()



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