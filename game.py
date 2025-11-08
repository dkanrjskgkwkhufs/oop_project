import pygame
from map import Map
from tower import Tower
from wave_manager import WaveManager
from base import Base

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("OOP Tower Defense")
        self.clock = pygame.time.Clock()
        self.running = True

        self.map = Map()
        self.base = Base((self.map.path[-1][0], self.map.path[-1][1]))  # 마지막 지점
        self.wave_manager = WaveManager(self.map.path)
        self.towers = [Tower((400, 300))]
        self.projectiles = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.base.is_destroyed():
            self.running = False
            print("Game Over!")
            return

        # 적 이동
        self.wave_manager.update(self.base)

        # 타워 공격
        for tower in self.towers:
            proj = tower.update(self.wave_manager.enemies)
            if proj:
                self.projectiles.append(proj)

        # 투사체 이동
        for proj in self.projectiles[:]:
            proj.update()
            if not proj.alive:
                self.projectiles.remove(proj)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.map.draw(self.screen)
        self.base.draw(self.screen)
        self.wave_manager.draw(self.screen)
        for tower in self.towers:
            tower.draw(self.screen)
        for proj in self.projectiles:
            proj.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
