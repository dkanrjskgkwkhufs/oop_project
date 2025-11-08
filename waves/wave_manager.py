from enemy.enemy import Enemy

class WaveManager:
    def __init__(self, path, total_enemies):
        self.path = path
        self.enemies = []
        self.spawn_timer = 0
        self.interval = 90
        self.total_enemies = total_enemies
        self.spawned_enemies = 0


    def update(self, base):
        self.spawn_timer += 1
        if self.spawned_enemies < self.total_enemies and self.spawn_timer >= self.interval:
            self.spawn_timer = 0
            self.enemies.append(Enemy(self.path))
            self.spawned_enemies += 1
        for e in self.enemies[:]:
            e.update(base)
            if not e.alive:
                self.enemies.remove(e)

    def draw(self, screen):
        for e in self.enemies:
            e.draw(screen)

    def is_wave_cleared(self):
        return self.spawned_enemies >= self.total_enemies and len(self.enemies) == 0
