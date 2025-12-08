import pygame
from enemys.enemyinterface import EnemyInterface

class EnemySnooze(EnemyInterface):
    def __init__(self, path, damage=10, reward=10):
        self.path = path
        self.index = 0
        self.pos = list(path[0])
        self.hp = 70
        self.speed = 0.5
        self.alive = True
        self.damage = damage
        self.reward = reward
        self.image = pygame.image.load('assets/enemies/enemy_snooze.png').convert_alpha()
        size = 50
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, base):
        if self.index < len(self.path) - 1:
            target = self.path[self.index + 1]
            dx, dy = target[0] - self.pos[0], target[1] - self.pos[1]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist < self.speed:
                self.index += 1
            else:
                self.pos[0] += self.speed * dx / dist
                self.pos[1] += self.speed * dy / dist
            self.rect.center = (int(self.pos[0]), int(self.pos[1]))
        else:
            base.take_damage(self.damage)
            self.alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
            return True
        return False
    def apply_slow(self, rate: float):
        self.speed *= rate