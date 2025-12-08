import pygame

class TowerSelectionUI:
    def __init__(self):
        self.active = False
        self.options = ["자연과학관", "어문학관", "인문경상관", "학생회관", "ai융합대학"]
        self.images = {
            "자연과학관": pygame.image.load("assets/button/basic.png"),
            "어문학관": pygame.image.load("assets/button/slow.png"),
            "인문경상관": pygame.image.load("assets/button/gold.png"),
            "학생회관": pygame.image.load("assets/button/frenzy.png"),
            "ai융합대학": pygame.image.load("assets/button/laser.png"),
        }

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
            img = self.images[option]
            scaled = pygame.transform.smoothscale(img, (380, 210))
            img_rect = scaled.get_rect(topleft=(x, y))
            self.rects.append((option, scaled, img_rect))
            y += 160

    def handle_event(self, event):
        if not self.active:
            return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for option, img, rect in self.rects:
                if rect.collidepoint(event.pos):
                    if self.on_select:
                        self.on_select(option)
                    self.close()
                    return

    def draw(self, screen):
        if not self.active:
            return
        for option, img, rect in self.rects:
            screen.blit(img, rect)
