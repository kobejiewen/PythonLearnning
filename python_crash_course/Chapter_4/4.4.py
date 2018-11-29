# 使用列表的一部分

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:])
print(players[:4])
#负数索引返回离列表末尾相应距离的元素
print(players[-2:])

# 遍历切片
for player in players[:3]:
    print(player.title())

# 复制列表 [:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
