import pygame
import math

class Projectile:
    def __init__(self, pos, target, dmg):
        self.pos = list(pos)
        self.target = target
        self.dmg = dmg
        self.speed = 5
        self.alive = True

    def update(self):
        if not self.target.alive:
            self.alive = False
            return

        dx, dy = self.target.pos[0] - self.pos[0], self.target.pos[1] - self.pos[1]
        dist = math.hypot(dx, dy)
        if dist < self.speed:
            self.target.take_damage(self.dmg)
            self.alive = False
        else:
            self.pos[0] += self.speed * dx / dist
            self.pos[1] += self.speed * dy / dist

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.pos[0]), int(self.pos[1])), 4)
