from CircleShape import CircleShape
import constants
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.shot_cooldown_timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

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
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown_timer <= 0:
            # Use the same forward direction as in triangle()
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            
            # Position the shot at the front of the ship
            shot_x = self.position.x + direction.x * self.radius
            shot_y = self.position.y + direction.y * self.radius
            
            # Create the shot
            shot = Shot(shot_x, shot_y, self.rotation)
            
            # Set velocity - might need to negate if you want shots to go "forward"
            shot.velocity = direction * constants.PLAYER_SHOOT_SPEED
            
            # Add to group and reset cooldown
            self.shots_group.add(shot)
            self.shot_cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN