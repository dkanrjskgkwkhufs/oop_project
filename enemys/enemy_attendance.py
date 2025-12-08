import pygame
from enemys.enemyinterface import EnemyInterface

class EnemyAttendance(EnemyInterface):
    def __init__(self, path, damage=10, reward=10):
        self.path = path
        self.index = 0
        self.pos = list(path[0])
        self.hp = 40
        self.speed = 3
        self.alive = True
        self.damage = damage
        self.reward = reward
        self.invisible = False
        self.invisible_until = 0
        self.invisibility_triggered = False
        self.image = pygame.image.load('assets/enemies/enemy_attendance.png').convert_alpha()
        size = 70
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(center=self.pos)

        self.alpha = 255
    def start_invisibility(self, duration=3000):
        self.invisible = True
        self.invisible_until = pygame.time.get_ticks() + duration

    def update(self, base):
        now = pygame.time.get_ticks()
        if self.hp <= 20 and not self.invisibility_triggered:
            self.start_invisibility(3000)  # 3초
            self.invisibility_triggered = True
        if self.invisible and now >= self.invisible_until:
            self.invisible = False
        if self.invisible:
            if self.alpha > 80:
                self.alpha -= 8
        else:
            if self.alpha < 255:
                self.alpha += 8
        self.image.set_alpha(self.alpha)
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
        if self.invisible:
            return False
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
            return True
        return False

    def apply_slow(self, rate: float):
        if self.invisible:
            return False
        self.speed *= rate