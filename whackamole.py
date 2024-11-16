import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        x = 0
        y = 0
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    row = event.pos[0]//32
                    col = event.pos[1]//32
                    if row == x and col == y:
                        x = random.randrange(0, 20)
                        y = random.randrange(0, 16)

            screen.fill("light green")
            for i in range(32, 640, 32):
                pygame.draw.line(screen, "magenta", (i, 0), (i, 512))
            for i in range(32, 512, 32):
                pygame.draw.line(screen, "dark blue", (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x*32, y*32)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
