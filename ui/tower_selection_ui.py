import pygame

class TowerSelectionUI:
    def __init__(self):
        self.active = False
        self.options = ["basic"]
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
            rect = pygame.Rect(x, y, 100, 50)
            self.rects.append((option, rect))
            y += 60

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

        for option, rect in self.rects:
            pygame.draw.rect(screen, (100, 100, 100), rect)
            font = pygame.font.SysFont(None, 24)
            text = font.render(option, True, (255, 255, 255))
            screen.blit(text, (rect.x + 10, rect.y + 10))
