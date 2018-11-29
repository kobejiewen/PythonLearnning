# 元祖 ()
# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 不能给元组的元素赋值,但可以给存储元组的变量赋值
dimensions = (300, 350)

for dimension in dimensions:
    print(dimension)