import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Класс для управления ресурсом и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # windowed ###########
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        ######################
        # fullscreen ##########
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        ######################
        pygame.display.set_caption('Alien Invasion')
        self.bg_color = (self.settings.bg_color)
        self.ship = Ship(self)

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            self._update_screen()
            self._check_event()
            self.ship.moved_ship()
            self.clock.tick(60)

    def _update_screen(self):
        """Обновление экрана """
        # При каждом проходе цикла перерисовается экран
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Отоброжение последнего прорисованного экрана
        pygame.display.flip()

    def _check_event(self):
        """ Отслеживает срабатывание клавиатуры и мыши """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_event(event)      
            elif event.type == pygame.KEYUP:
                self._key_up_event(event)
                
    def _key_down_event(self, event):
        """События нажатие клавиши"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _key_up_event(self, event):
        """События отпускания клавиши"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False


if __name__ == '__main__':
    # Создание экземпляра класса игры и запуск
    ai = AlienInvasion()
    ai.run_game()