class Settings:
    """存储创建游戏当中的一些设置"""
    def __init__(self):
        """初始化一些游戏设置"""
        #背景设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度
        self.speed_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0 # 外星人设置

        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale

        # 记分
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

