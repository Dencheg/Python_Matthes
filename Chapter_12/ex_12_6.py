import pygame
import sys
import time


speed = 0
accel = 1

while speed < 100:
    if accel < 5:
        accel += 1
    if speed <= 30:
        speed += accel
    if 60 >= speed > 30:
        speed += accel + accel
    if 100 >= speed > 60:
        speed += accel + accel + accel
    time.sleep(0.1)
    print(f'{speed} {accel}')
        # Прибавляем шаг, но не позволяем превысить max_speed
    speed = min(speed + step, max_speed)

class Airship:
    """Описание и управление самолетом"""

    def __init__(self, sky):
        """Инициализация атрибутов самолета"""
        self.screen = sky.screen
        self.screen_rect = sky.screen.get_rect()

        # Сохраняем оригинал картинки, чтобы качество не портилось при вращении
        self.raw_image = pygame.image.load('Tu2.png').convert_alpha() # Конвертируем альфа канал?
        # Обрезаем лишнюю прозрачность вокруг самолёта:
        self.orig_image = self.raw_image.subsurface(self.raw_image.get_bounding_rect()).copy()
        self.angle = -90
        self.rotation_speed = 3
        self.speed = 0
        self.flag_speed = False

        # Сразу поворачиваем в начальное положение и выставляем центр
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(midleft = self.screen_rect.midleft)

        # Маска для точных столкновений по контуру самолёта
        self.airship_mask = pygame.mask.from_surface(self.image)

        # Точные координаты центра (для плавного движения)
        self.pos = pygame.math.Vector2(self.rect.center)


        self.flag_right = False
        self.flag_left = False


        
                
    
    def blit_ship(self):
        self.screen.blit(self.image, self.rect)

    def moved(self):

        if self.flag_right == True:
            self.angle += 1
        if self.flag_left == True:
            self.angle -= 1

        # 2. Вычисляем вектор, куда сейчас смотрит нос самолёта
        # (0, -1) — это направление "вверх" на исходной картинке Tu2.png.
        # Знак минус перед self.angle нужен, так как в Vector2 угол считается по часовой стрелке,
        # а в pygame.transform.rotate — против часовой.
        direction = pygame.math.Vector2(0, -1).rotate(-self.angle)

        self.pos += direction * self.speed
        
        # 1. Поворачиваем ОРИГИНАЛ
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
         # 2. Пересчитываем rect с привязкой к текущему центру
        self.rect = self.image.get_rect(center=self.pos)
        # 3. Обновляем маску под новый угол
        self.airship_mask = pygame.mask.from_surface(self.image)

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
                        self.airship.speed += 1
                    if event.key == pygame.K_DOWN:
                        self.airship.speed -= 1
                    if event.key == pygame.K_LEFT:
                        self.airship.flag_left = True
                    if event.key == pygame.K_RIGHT:
                        self.airship.flag_right = True
                    if event.key == pygame.K_SPACE:
                        if self.airship.flag_speed == False:
                            self.airship.flag_speed = True
                        elif self.airship.flag_speed == True:
                            self.airship.flag_speed = False
                    print(self.airship.flag_speed)
                    print(pygame.key.name(event.key)) # ex.12.5 с доработкой
                    print(self.airship.speed)
                elif event.type == pygame.KEYUP:
                    # if event.key == pygame.K_UP:
                    #     self.airship.flag_up = False
                    # if event.key == pygame.K_DOWN:
                    #     self.airship.flag_down = False
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