import pygame

class TowerSelectionUI:
    def __init__(self):
        self.active = False
        self.options = ["자연과학관", "어문학관"]
        self.introduction = [
            "모든 학문의 기초가 되는 자연 과학처럼 기본적인 타워",
            "복잡한 문법체계가 적들을 얼어붙게 만듭니다."
        ]

        self.rects = []
        self.on_select = None

    def open(self, on_select_callback):
        self.active = True
        self.on_select = on_select_callback
        self.create_buttons()

    def close(self):
        self.active = False
        self.on_select = None

    def create_buttons(self):
        self.rects = []
        x, y = 100, 100
        for option in self.options:
            rect = pygame.Rect(x, y, 120, 50)
            self.rects.append((option, rect))
            y += 90

    def handle_event(self, event):
        if not self.active:
            return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for option, rect in self.rects:
                if rect.collidepoint(event.pos):
                    if self.on_select:
                        self.on_select(option)
                    self.close()
                    return

    def draw(self, screen):
        if not self.active:
            return

        font_title = pygame.font.Font("C:/Windows/Fonts/malgun.ttf", 16)
        font_intro = pygame.font.Font("C:/Windows/Fonts/malgun.ttf", 10)

        for (option, rect), intro in zip(self.rects, self.introduction):
            pygame.draw.rect(screen, (100, 100, 100), rect)

            # 타워 이름
            text = font_title.render(option, True, (255, 255, 255))
            screen.blit(text, (rect.x + 10, rect.y + 10))

            # 설명
            intro_text = font_intro.render(intro, True, (230, 230, 230))
            screen.blit(intro_text, (rect.x, rect.y + 55))
