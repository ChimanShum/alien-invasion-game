import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """代表单个外星人的类"""
    def __init__(self, ai_game):
        """初始化外星人并设置它的起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图形并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # 外星人掉落的速度
        # fleet_direction为1代表向右移，为-1表示向左移
        self.fleet_direction = 1

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
    def update(self):
        """向左向右移动外星人"""
        self.x += (self.settings.alien_speed * 
                   self.settings.fleet_direction) # 方向和速度的乘积代表其走向
        self.rect.x = self.x

    
