from CircleShape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), constants.SHOT_RADIUS, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        # Check if the shot is off-screen (adjust screen width/height as needed)
        if (self.position.x < 0 or self.position.x > constants.SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > constants.SCREEN_HEIGHT):
            self.kill()  # Remove from sprite group