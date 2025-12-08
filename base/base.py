import pygame

class Base:
    def __init__(self, position, hp=200):
        self.position = position
        self.max_hp = hp
        self.hp = hp
        self.image = pygame.image.load("assets/base.png").convert_alpha()
        size = 100
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(center=self.position)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_destroyed(self):
        return self.hp <= 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        bar_w = 60
        bar_h = 8
        ratio = self.hp / self.max_hp

        bar_x = self.position[0] - bar_w // 2
        bar_y = self.position[1] - self.rect.height // 2 - 15

        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_w, bar_h))
        pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, int(bar_w * ratio), bar_h))
