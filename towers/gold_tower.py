import math
import time
import pygame
from projectile.gold_projectile import GoldProjectile
from towers.tower_interface import TowerInterface


class GoldTower(TowerInterface):
    COST = 60

    def __init__(self, pos):
        self.pos = pos
        self.range = 150
        self.damage = 20
        self.cooldown = 1.0
        self.last_shot = 0
        self.image = pygame.image.load("assets/building/finance.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect(center=self.pos)
    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        self._pos = (int(value[0]), int(value[1]))
    @property
    def cost(self):
        return GoldTower.COST

    def update(self, enemies, player):
        now = time.time()
        if now - self.last_shot < self.cooldown:
            return None

        for e in enemies:
            if math.dist(self.pos, e.pos) <= self.range:
                self.last_shot = now
                return GoldProjectile(self.pos, e, self.damage, 2, player)
        return None

    def draw(self, screen):
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (50, 100, 50), self.pos, self.range, 1)
