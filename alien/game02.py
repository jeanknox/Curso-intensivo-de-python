import os, pygame, sys
class Settings():
    def __init__(self):
        self.scren_width = 1200
        self.scren_height = 800
        self.bg_color = (230,230,230)

class Chip():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("imagens/espaconave.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    ai_settings = Settings()
    ship = Chip(ai_settings)
    pygame.display.set_caption("Invasion Of The Hue")
    screen = pygame.display.set_mode((ai_settings.scren_width,ai_settings.scren_height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                ship.blitme()
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()

run_game()
