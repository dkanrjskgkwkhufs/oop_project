from wave_manager import WaveManager

class Level:
    def __init__(self, number, map_type, waves=10):
        self.number = number
        self.map_type = map_type
        self.waves = waves  # 한 레벨에서 총 스폰할 적 수

class LevelManager:
    def __init__(self):
        self.levels = [
            Level(1, "straight", waves=5),
            Level(2, "zigzag", waves=5),
            Level(3, "zigzag", waves=5)
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
            from straight_map import StraightMap
            game_map = StraightMap()
        elif level.map_type == "zigzag":
            from zigzag_map import ZigZagMap
            game_map = ZigZagMap()
        else:
            raise ValueError("Unknown map type")

        self.current_wave_manager = WaveManager(game_map.get_path(), total_enemies=level.waves)

        return game_map, self.current_wave_manager
