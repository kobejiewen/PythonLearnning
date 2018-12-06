import  sys
import pygame
from settings import Settings

def run_gamne():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色
    bg_color = (ai_setting.bg_color)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            # 玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT 事件，而我们调用sys.exit()来退出游戏
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕
        screen.fill(bg_color)

        # 在我们移动游戏元素时， pygame.display.flip() 将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
        pygame.display.flip()

run_gamne()