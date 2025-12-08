import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.show_intro()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
