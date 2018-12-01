# 用户输入和while循环
# 函数input()的工作原理

def input1():
    name = input("input your name: ")  # 函数input() 时， Python将用户输入解读为字符串
    print("your name is "+name)

def input2():
    prompt = "If you tell us who you are, we can personalize the messages you see."
    prompt += "\nWhat is your first name? "  # 运算符+= 在存储在prompt 中的字符串末尾附加一个字符串
    name = input(prompt)
    print("\nHello, " + name + "!")

# 函数int() 将数字的字符串表示转换为数值
def input3():
    age = input("how old are you : ")
    age = int(age)
    if age >= 20 :
        print("true")
    else:
        print("false")

# 求模运算符(%),它将两个数相除并返回余数
print(4%3)
print(6%3)
print(1%3)

# even偶数,odd奇数
def even_or_odd():
    number = input("Enter a number, and I'll tell you if it's even or odd: ")
    number = int(number)
    if number % 2 == 0:
        print("\nThe number " + str(number) + " is even.")
    else:
        print("\nThe number " + str(number) + " is odd.")
even_or_odd()



