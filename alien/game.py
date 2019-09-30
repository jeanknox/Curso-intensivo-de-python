import os, pygame, sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))
    pygame.display.set_caption("Invasao do hue")

    bg_color = (230,230,230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()

run_game()
