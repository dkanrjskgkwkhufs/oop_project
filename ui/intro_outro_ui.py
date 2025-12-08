import time

import pygame


class IntroOutroUI:

    def __init__(self, width, height, screen, clock):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = screen
        self.clock = clock
    def show_intro(self):
        images = [
            pygame.image.load("assets/intro/intro1.png"),
            pygame.image.load("assets/intro/intro2.png"),
            pygame.image.load("assets/intro/intro3.png"),
            pygame.image.load("assets/intro/intro4.png"),
            pygame.image.load("assets/intro/intro5.png"),
            pygame.image.load("assets/intro/intro6.png"),
            pygame.image.load("assets/intro/intro7.png"),
            pygame.image.load("assets/intro/intro8.png")
        ]
        scaled_images = [pygame.transform.scale(img, (self.WIDTH, self.HEIGHT)) for img in images]
        for img in scaled_images:
            start = time.time()
            while time.time() - start < 3:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                self.screen.blit(img, (0, 0))
                pygame.display.flip()
                self.clock.tick(60)

    def show_outro(self):
        images = [
            pygame.image.load("assets/outro/ending_success.png"),
            pygame.image.load("assets/outro/last_ending.png")
        ]

        scaled_images = [pygame.transform.scale(img, (self.WIDTH, self.HEIGHT)) for img in images]

        for img in scaled_images:
            start = time.time()
            while time.time() - start < 3:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                self.screen.blit(img, (0, 0))
                pygame.display.flip()
                self.clock.tick(60)
    def show_fail_outro(self):
        images = [
            pygame.image.load("assets/outro/ending_fail.png"),
            pygame.image.load("assets/outro/last_sad_ending.png")
        ]

        scaled_images = [pygame.transform.scale(img, (self.WIDTH, self.HEIGHT)) for img in images]

        for img in scaled_images:
            start = time.time()
            while time.time() - start < 3:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                self.screen.blit(img, (0, 0))
                pygame.display.flip()
                self.clock.tick(60)