import pygame
from player import Player
from enemy import Enemy
from score import Score

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.enemies = pygame.sprite.Group()
        self.score = Score()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.player.handle_event(event)
            self.update()
            self.draw()
        pygame.quit()

    def update(self):
        self.player.update()
        self.enemies.update()
        self.score.update(self.player, self.enemies)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()
