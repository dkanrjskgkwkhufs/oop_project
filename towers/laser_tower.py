import pygame
import math
import time

from towers.tower_interface import TowerInterface


class LaserTower(TowerInterface):
    COST = 100
    def __init__(self, pos):
        self.pos = pos
        self.range = 100
        self.base_damage = 0.5
        self.damage = self.base_damage
        self.damage_gain = 0.3
        self.tick_rate = 0.1
        self.last_tick = 0
        self.target = None
        self.laser_disconnect_time = 0.5
        self.image = pygame.image.load("assets/building/ai.png").convert_alpha()
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
        return LaserTower.COST

    def find_target(self, enemies):
        valid = [e for e in enemies if e.alive and math.dist(self.pos, e.pos) <= self.range]
        if not valid:
            return None
        return min(valid, key=lambda e: math.dist(self.pos, e.pos))

    def update(self, enemies, player):
        now = time.time()

        if not self.target or not self.target.alive or math.dist(self.pos, self.target.pos) > self.range:
            self.target = self.find_target(enemies)
            self.damage = self.base_damage
            self.last_tick = now
            return None

        if now - self.last_tick >= self.tick_rate:
            self.last_tick = now
            killed = self.target.take_damage(self.damage)
            self.damage += self.damage_gain

            if killed:
                player.earn_gold(self.target.reward)
                player.score += self.target.reward
                self.target = None
                self.damage = self.base_damage

        return None

    def draw(self, screen):
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (40, 80, 150), self.pos, self.range, 1)

        if self.target and self.target.alive:
            pygame.draw.line(
                screen,
                (255, 80, 80),
                self.pos,
                (int(self.target.pos[0]), int(self.target.pos[1])),
                3
            )