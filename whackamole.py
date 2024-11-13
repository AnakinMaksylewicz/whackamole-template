"""
Anakin Maksylewicz
COP3502C
11/12/2024
Whack-a-mole game

"""

import pygame
from random import randrange


def main():
    #Constants
    SQUARE_WIDTH = 32
    BOARD_ROWS = 16
    BOARD_COLS = 20
    LINE_COLOR = (0, 0, 0)
    moleX = moleY = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft=(moleX, moleY))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #This is the position of where the user has clicked. Int division by 32 to compare exact rectangle (i.e. a click on 64, 32 would be the rectangle
                    #in position 2, 1).
                    mouseX = event.pos[0] // 32
                    mouseY = event.pos[1] // 32
                    #If the user has clicked on the mole rectangle (which we divide by 32 to compare correctly), reassign mole x and mole y using randrange() and
                    #use mole_rect.topleft to reassign because mole_rect is an OBJECT. If I try to do mole_rect = mole_image.get_rect(topleft=(moleX, moleY)), I would
                    #be creating a new instance of Rect, which wouldn't work.
                    if mouseX == moleX // SQUARE_WIDTH and mouseY == moleY // SQUARE_WIDTH:
                        moleX = randrange(BOARD_COLS) * SQUARE_WIDTH
                        moleY = randrange(BOARD_ROWS) * SQUARE_WIDTH
                        mole_rect.topleft = (moleX, moleY)
            screen.fill("light green")
            #Draw grid
            for i in range(BOARD_COLS):
                pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_WIDTH, 0),
                                 (i * SQUARE_WIDTH, SQUARE_WIDTH * BOARD_ROWS))
            for j in range(BOARD_ROWS):
                pygame.draw.line(screen, LINE_COLOR, (0, j * SQUARE_WIDTH),
                                 (SQUARE_WIDTH * BOARD_COLS, j * SQUARE_WIDTH))
            screen.blit(mole_image, mole_rect)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
