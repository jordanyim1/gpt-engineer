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
            pygame.sprite.groupcollide(self.player.bullets, self.enemies, True, True)
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                running = False  # End the game if the player collides with an enemy

            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

    def spawn_enemy(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)

if __name__ == "__main__":
    game = Game()
    game.run()