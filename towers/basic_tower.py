import math
import time
import pygame
from projectile.projectile import Projectile
from towers.tower_interface import TowerInterface


class BasicTower(TowerInterface):
    COST = 50

    def __init__(self, pos):
        self.pos = pos
        self.range = 150
        self.damage = 20
        self.cooldown = 1.0
        self.last_shot = 0

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        # value는 보통 (x, y) tuple
        # tuple로 강제 변환
        self._pos = (int(value[0]), int(value[1]))
    @property
    def cost(self):
        return BasicTower.COST

    def update(self, enemies, player):
        now = time.time()
        if now - self.last_shot < self.cooldown:
            return None

        for e in enemies:
            if math.dist(self.pos, e.pos) <= self.range:
                self.last_shot = now
                return Projectile(self.pos, e, self.damage, player)
        return None

    def draw(self, screen):
        pygame.draw.circle(screen, (100, 200, 100), self.pos, 15)
        pygame.draw.circle(screen, (50, 100, 50), self.pos, self.range, 1)
