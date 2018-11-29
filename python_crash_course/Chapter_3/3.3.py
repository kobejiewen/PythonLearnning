# 3.3组织列表

#方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#函数sorted()对列表进行临时排序
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars2))

#reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
cars2.reverse()
print(cars2)
print(cars2.__len__())
print(len(cars2))