class Settings:
    """Класс для хранение настроек игры 'Инопланетное вторжение'"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230) 
        self.ship_speed = 1.5
        # bullet
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3