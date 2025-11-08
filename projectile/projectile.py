import pygame
import math

class Projectile:
    def __init__(self, pos, target, dmg, player=None):
        self.pos = list(pos)
        self.target = target
        self.dmg = dmg
        self.speed = 5
        self.alive = True
        self.player = player  # 💰 추가

    def update(self):
        if not self.target.alive:
            self.alive = False
            return

        dx, dy = self.target.pos[0] - self.pos[0], self.target.pos[1] - self.pos[1]
        dist = math.hypot(dx, dy)
        if dist < self.speed:
            killed = self.target.take_damage(self.dmg)
            if killed and self.player:
                self.player.earn_gold(self.target.reward)
                self.player.score += 10
            self.alive = False
        else:
            self.pos[0] += self.speed * dx / dist
            self.pos[1] += self.speed * dy / dist

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.pos[0]), int(self.pos[1])), 4)
