import math
import time
import pygame
from projectile.basic_projectile import BasicProjectile

from towers.tower_interface import TowerInterface


class FrenzyTower(TowerInterface):
    COST = 80

    def __init__(self, pos):
        self.pos = pos
        self.range = 150
        self.damage = 15
        self.cooldown = 1.2
        self.min_cooldown = 0.15
        self.cooldown_reduction = 0.05  # 발사마다 줄어드는 쿨타임
        self.last_shot = 0
        self.image = pygame.image.load("assets/building/club.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=self.pos)

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        self._pos = (int(value[0]), int(value[1]))

    @property
    def cost(self):
        return FrenzyTower.COST

    def update(self, enemies, player):
        now = time.time()
        if now - self.last_shot < self.cooldown:
            return None

        for e in enemies:
            if math.dist(self.pos, e.pos) <= self.range:
                self.last_shot = now
                self.cooldown = max(self.min_cooldown, self.cooldown - self.cooldown_reduction)
                return BasicProjectile(self.pos, e, self.damage, player)

        return None

    def draw(self, screen):
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (120, 40, 40), self.pos, self.range, 1)
