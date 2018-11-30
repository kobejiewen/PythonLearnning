# 使用字典
# 字典是一种动态结构，可随时在其中添加键—值对

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)
alien_1['color']='yellow'
print(alien_1)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# del 语句将相应的键—值对彻底删除
del alien_0['x_position']
print("del "+str(alien_0))

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# print分行
print("phil's favorite language is " +
    favorite_languages['phil'].title() +
    ".")

