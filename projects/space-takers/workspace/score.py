import pygame

class Score:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def update(self, player, enemies):
        hits = pygame.sprite.groupcollide(player.bullets, enemies, True, True)
        self.score += len(hits) * 10

    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
