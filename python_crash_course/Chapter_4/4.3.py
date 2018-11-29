# 创建数值列表

for vl in range(1,5):
    print(vl)

# 使用range() 创建数字列表,函数list() 将range() 的结果直接转换为列表
number=list(range(1,6))
print(number)

# 打印1~10内的偶数,range() 从2开始数，然后不断地加2，直到达到或超过终值（11）
even_numbers=list(range(2,11,2))
print(even_numbers)

#
squares=[]
for value in range(1,11):
    #square=value**2
    squares.append(value**2)
print(squares)

# 对数字列表执行简单的统计计算
digits=[1,2,3,4,5,6]
print("最小值"+str(min(digits)))
print(max(digits))
print(sum(digits))

# 列表解析
squares2 = [val**2 for val in range(1,11)]
print(squares2)