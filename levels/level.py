class Level:
    def __init__(self, number, map_type, waves=10, enemy_types=None):
        self.number = number
        self.map_type = map_type
        self.waves = waves
        self.enemy_types = enemy_types or []
