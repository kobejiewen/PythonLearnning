# 简单回顾

"""
12.7.1 alien_invasion.py
主文件alien_invasion.py创建一系列整个游戏都要用到的对象：存储在ai_settings 中的设置、存储在screen 中的主显示surface以及一个飞船实例。文件alien_invasion.py还包含游
戏的主循环，这是一个调用check_events() 、 ship.update() 和update_screen() 的while 循环。
要玩游戏《外星人入侵》，只需运行文件alien_invasion.py。其他文件（settings.py、 game_functions.py、 ship.py）包含的代码被直接或间接地导入到这个文件中。

12.7.2 settings.py
文件settings.py包含Settings 类，这个类只包含方法__init__() ，它初始化控制游戏外观和飞船速度的属性。

12.7.3 game_functions.py
文件game_functions.py包含一系列函数，游戏的大部分工作都是由它们完成的。函数check_events() 检测相关的事件，如按键和松开，并使用辅助函
数check_keydown_events() 和check_keyup_events() 来处理这些事件。就目前而言，这些函数管理飞船的移动。模块game_functions 还包含函
数update_screen() ，它用于在每次执行主循环时都重绘屏幕。

12.7.4 ship.py
文件ship.py包含Ship 类，这个类包含方法__init__() 、管理飞船位置的方法update() 以及在屏幕上绘制飞船的方法blitme() 。表示飞船的图像存储在文件夹images下的
文件ship.bmp中。
"""