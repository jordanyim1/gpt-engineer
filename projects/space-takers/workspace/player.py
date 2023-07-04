import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25)
        self.rect = self.image.get_rect(center=(50, 300))  # Player spawns on the left of the screen
        self.bullets = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
        if keys[pygame.K_SPACE] and not self.bullets:  # Only spawn a bullet if there are no bullets on the screen
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)
