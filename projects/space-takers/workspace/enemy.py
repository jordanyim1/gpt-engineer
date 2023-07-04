import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        pygame.draw.rect(self.image, (255, 0, 0), (0, 0, 50, 50))
        self.rect = self.image.get_rect(topleft=(800, 300))

    # ... rest of the class remains the same ...
