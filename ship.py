import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船类别"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        
        # 在飞船的属性x存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # 对于每一艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动的标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed  # 上述方法是为了让飞机隔墙不超出范围
        if self.moving_top and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

        # 根据self.x更新rect对象
        # self.rect.x = self.x  # 单纯在窗口随机位置生成飞机使用

    def center_ship(self):
        """让飞船在屏幕中居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
