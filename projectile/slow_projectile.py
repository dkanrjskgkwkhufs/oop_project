import pygame
import math

class SlowProjectile:
    def __init__(self, pos, target, slow_rate, dmg, player=None):
        self.pos = list(pos)
        self.target = target
        self.slow_rate = slow_rate
        self.damage = dmg
        self.speed = 5
        self.alive = True
        self.player = player

    def update(self):
        if not self.target.alive:
            self.alive = False
            return

        dx = self.target.pos[0] - self.pos[0]
        dy = self.target.pos[1] - self.pos[1]
        dist = math.hypot(dx, dy)

        if dist < self.speed:
            self.target.apply_slow(self.slow_rate)
            self.target.take_damage(self.damage)
            self.alive = False
            return

        self.pos[0] += self.speed * dx / dist
        self.pos[1] += self.speed * dy / dist

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 150, 255), (int(self.pos[0]), int(self.pos[1])), 4)
