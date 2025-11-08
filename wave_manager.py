from enemy import Enemy

class WaveManager:
    def __init__(self, path):
        self.path = path
        self.enemies = []
        self.spawn_timer = 0
        self.interval = 90

    def update(self, base):
        self.spawn_timer += 1
        if self.spawn_timer >= self.interval:
            self.spawn_timer = 0
            self.enemies.append(Enemy(self.path))

        for e in self.enemies[:]:
            e.update(base)
            if not e.alive:
                self.enemies.remove(e)

    def draw(self, screen):
        for e in self.enemies:
            e.draw(screen)
