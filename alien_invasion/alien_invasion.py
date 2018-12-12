import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_gamne():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_setting,screen)

    # 创建一个外星人
    alien = Alien(ai_setting,screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_setting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting,screen,ship,alien,bullets)

        # 删除已消失的子弹
        for bullet in bullets:
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)

        # 每次循环都重绘屏幕
        gf.update_screen(ai_setting,screen,ship,alien,bullets)


run_gamne()

