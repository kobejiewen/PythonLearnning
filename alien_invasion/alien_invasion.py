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
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船,创建一个用于存储子弹、外星人的编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship,aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

        # 删除已消失的子弹
        for bullet in bullets:
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)

        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_gamne()

