import pygame

class Ship:
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его изначальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()     
        
        # Каждый новый корабль появляется у нижнего экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Перевод значения положения
        self.x = float(self.rect.x)

        # Флаги перемещения корабля
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает корабль влево или вправо"""
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Передач обработанного значения
        self.rect.x = self.x