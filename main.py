import pygame
from constants import *
from player import Player  # Import the Player class directly
from CircleShape import CircleShape                    

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the main() function and close the program
                
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        
        # Only call clock.tick once - this line both limits the framerate and returns the time passed
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    print("About to start main")
    main()
    print("Main has returned")