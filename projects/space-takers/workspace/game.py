import pygame
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.enemies = pygame.sprite.Group()
        self.spawn_enemy_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawn_enemy_event, 1000)  # Spawn enemy every 1 second
        self.score = 0  # Add score attribute
        self.font = pygame.font.Font(None, 36)  # Font to display the score

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self.spawn_enemy_event:
                    self.spawn_enemy()

            self.player.update()
            self.player.bullets.update()
            self.enemies.update()

            # Collision detection
            for bullet in pygame.sprite.groupcollide(self.player.bullets, self.enemies, True, True):
                self.score += 1  # Increment score when an enemy is killed

            if pygame.sprite.spritecollideany(self.player, self.enemies):
                running = False  # End the game if the player collides with an enemy

            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)

            # Draw score
            score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_text, (650, 10))

            pygame.display.flip()

        pygame.quit()

    def spawn_enemy(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)

if __name__ == "__main__":
    game = Game()
    game.run()