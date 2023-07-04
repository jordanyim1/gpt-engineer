import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25)
        self.rect = self.image.get_rect(center=(800, random.randint(50, 550)))
        self.x = self.rect.x
        self.y = self.rect.y
        self.amplitude = random.randint(1, 5)
        self.frequency = random.uniform(0.01, 0.05)

    def update(self):
        self.x -= 2
        self.y += self.amplitude * math.sin(self.frequency * self.x)
        self.rect.center = (self.x, self.y)
        if self.rect.right < 0:
            self.kill()
