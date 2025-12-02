from waves.wave_manager import WaveManager
from maps.straight_map import StraightMap
from maps.zigzag_map import ZigZagMap
from enemy.fast_enemy import FastEnemy
from enemy.enemy import Enemy


class Level:
    def __init__(self, number, map_type, waves=10, enemy_types=None):
        self.number = number
        self.map_type = map_type
        self.waves = waves
        self.enemy_types = enemy_types or []


class LevelManager:
    def __init__(self):
        self.levels = [
            Level(1, "straight", waves=5, enemy_types=[(Enemy, 1)]),
            Level(2, "zigzag", waves=10, enemy_types=[(FastEnemy, 1)]),
            Level(3, "zigzag", waves=20, enemy_types=[(Enemy, 70), (FastEnemy, 30)])
        ]
        self.current_level_index = 0
        self.current_wave_manager = None

    def get_current_level(self):
        return self.levels[self.current_level_index]

    def next_level(self):
        if self.current_level_index + 1 < len(self.levels):
            self.current_level_index += 1
            return True
        return False  # 더 이상 레벨 없음

    def load_map_and_wave(self):
        level = self.get_current_level()
        if level.map_type == "straight":
            game_map = StraightMap()
        elif level.map_type == "zigzag":
            game_map = ZigZagMap()
        else:
            raise ValueError("Unknown map type")
        self.current_wave_manager = WaveManager(
            game_map.get_path(),
            total_enemies=level.waves,
            enemy_types=level.enemy_types
        )
        return game_map, self.current_wave_manager
