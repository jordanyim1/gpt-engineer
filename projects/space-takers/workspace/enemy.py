import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect(topleft=(800, 300))

    def update(self):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.kill()
