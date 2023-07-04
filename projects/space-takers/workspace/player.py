import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25)
        self.rect = self.image.get_rect(center=(400, 300))
        self.bullets = pygame.sprite.Group()

    # ... rest of the class remains the same ...
