import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0), (5, 5), 5)
        self.rect = self.image.get_rect(center=player.rect.center)

    # ... rest of the class remains the same ...
