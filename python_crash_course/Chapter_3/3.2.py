# 列表 增删改
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0]='terk'
bicycles.append('ducati')
bicycles.insert(0,'moto')
del bicycles[2]
rm='specialized'
bicycles.remove(rm)
print(bicycles)
print("removed "+rm)
print(bicycles[0].title())
print(bicycles[-1])

# pop删除列表末尾的元素，并让你能够接着使用它
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
pop_motorcycle = motorcycles.pop(1)
print(popped_motorcycle)
print(pop_motorcycle)
print(motorcycles)

