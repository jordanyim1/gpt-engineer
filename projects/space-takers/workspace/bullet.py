import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect(center=player.rect.center)

    def update(self):
        self.rect.x += 5
        if self.rect.left > 800:
            self.kill()
