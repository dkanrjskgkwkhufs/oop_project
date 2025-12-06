import math
import time
import pygame
from projectile.slow_projectile import SlowProjectile
from towers.tower_interface import TowerInterface


class SlowTower(TowerInterface):
    COST = 40

    def __init__(self, pos):
        self.pos = pos
        self.range = 150
        self.slow_rate = 0.5
        self.dmg = 10
        self.cooldown = 1.2
        self.last_shot = 0
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = (int(value[0]), int(value[1]))

    @property
    def cost(self):
        return SlowTower.COST

    def update(self, enemies, player):
        now = time.time()
        if now - self.last_shot < self.cooldown:
            return None

        for e in enemies:
            if math.dist(self.pos, e.pos) <= self.range:
                self.last_shot = now
                return SlowProjectile(
                    pos=self.pos,
                    target=e,
                    slow_rate=self.slow_rate,
                    dmg=self.dmg,
                    player=player
                )
        return None

    def draw(self, screen):
        pygame.draw.circle(screen, (100, 180, 255), self.pos, 15)  # 파란 계열
        pygame.draw.circle(screen, (80, 140, 200), self.pos, self.range, 1)
