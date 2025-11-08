import pygame
import math
import time
from projectile.projectile import Projectile

class Tower:
    COST = 50

    def __init__(self, pos):
        self.pos = pos
        self.range = 150
        self.damage = 20
        self.cooldown = 1.0
        self.last_shot = 0

    def update(self, enemies, player):
        now = time.time()
        if now - self.last_shot < self.cooldown:
            return None

        for e in enemies:
            dist = math.dist(self.pos, e.pos)
            if dist <= self.range:
                self.last_shot = now
                return Projectile(self.pos, e, self.damage, player)
        return None

    def draw(self, screen):
        pygame.draw.circle(screen, (100, 200, 100), self.pos, 15)
        pygame.draw.circle(screen, (50, 100, 50), self.pos, self.range, 1)
