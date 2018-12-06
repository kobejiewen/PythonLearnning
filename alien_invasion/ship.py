import  pygame

class Ship():

    def __init__(self,screen):
        """初始化飞船并设置起初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        # load()函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image中
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

# 注意在Pygame中，原点(0, 0)位于屏幕左上角
