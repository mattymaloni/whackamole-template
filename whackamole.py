import pygame
import random


def main():
    try:
        pygame.init()

        # loads mole image
        mole_image = pygame.image.load("mole.png")
        square_size = 32  # Size of each grid square

        window_size = (640, 512)
        screen = pygame.display.set_mode(window_size)
        clock = pygame.time.Clock()
        black = (0, 0, 0)
        light_green = (144, 238, 144)  # RGB for light green

        # mole starting posotion
        mole_x = 0
        mole_y = 0

        running = True
        while running:
            # draws the grid
            for x in range(0, window_size[0], square_size):
                pygame.draw.line(screen, black, (x, 0), (x, window_size[1]))
            for y in range(0, window_size[1], square_size):
                pygame.draw.line(screen, black, (0, y), (window_size[0], y))

            # draws the mole
            screen.blit(mole_image, (mole_x, mole_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mole's rectangle
                    mole_rect = pygame.Rect(mole_x, mole_y, square_size, square_size)

                    # check mouse click
                    if mole_rect.collidepoint(event.pos):
                        # moves the mole
                        mole_x = random.randrange(0, window_size[0] // square_size) * square_size
                        mole_y = random.randrange(0, window_size[1] // square_size) * square_size

            # creates screen
            screen.fill(light_green)



            # Update the display
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
