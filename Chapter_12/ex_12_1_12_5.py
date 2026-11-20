# ex.12.2
import pygame
import sys

class Airship:
    """Описание и управление самолетом"""

    def __init__(self, sky):
        """Инициализация атрибутов самолета"""
        self.screen = sky.screen
        self.screen_rect = sky.screen.get_rect()

        self.image = pygame.image.load('Tu2.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.flag_right = False
        self.flag_left = False
        self.flag_up = False
        self.flag_down = False  

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)

    def moved(self):
        # ex.12.4
        if self.flag_right == True:
            self.rect.x += 1
        if self.flag_left == True:
            self.rect.x -= 1
        if self.flag_up == True:
            self.rect.y -= 1
        if self.flag_down == True:
            self.rect.y += 1

# ex.12.1
class Sky:
    """Выводит лазурное небо"""

    def __init__(self):
        """Инициализирует атрибуты"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = 0, 127, 255
        pygame.display.set_caption('Sky')
        self.clock = pygame.time.Clock()
        self.airship = Airship(self)

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.airship.flag_up = True
                    if event.key == pygame.K_DOWN:
                        self.airship.flag_down = True
                    if event.key == pygame.K_LEFT:
                        self.airship.flag_left = True
                    if event.key == pygame.K_RIGHT:
                        self.airship.flag_right = True
                    print(pygame.key.name(event.key)) # ex.12.5 с доработкой
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.airship.flag_up = False
                    if event.key == pygame.K_DOWN:
                        self.airship.flag_down = False
                    if event.key == pygame.K_LEFT:
                        self.airship.flag_left = False
                    if event.key == pygame.K_RIGHT:
                        self.airship.flag_right = False
                    # print(event.key) # ex.12.5

            self.airship.moved()
            pygame.display.flip()
            self.screen.fill(self.bg_color)
            self.airship.blit_ship()
            self.clock.tick(60)

if __name__ == '__main__':
    sk = Sky()
    sk.run_game()

# ex.12.3 принял к свкдкению