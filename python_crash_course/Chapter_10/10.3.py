# 异常

# 处理ZeroDivisionError 异常
# print(5/0) # ZeroDivisionError 是一个异常对象

# 使用try-except 代码块
def test1():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")
#test1()

# 使用异常避免崩溃,else代码块
def test2():
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by zero!")
        else:
            print(answer)
#test2()

# 处理FileNotFoundError 异常
def test3():
    filename = 'alice.txt'
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg="Sorry, the file " + filename + " does not exist."
        print(msg)
#test3()

# 分析文本，方法split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中
def test4():
    filename = 'Alice.txt'
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        print()
    else:
        num = len(contents.split())
        print("The file " + filename + " has about " + str(num) + " words.")
#test4()

# 使用多个文件
def count_words(fileName):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(fileName) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + fileName + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + fileName + " has about " + str(num_words) +" words.")

def test5():
    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
    for filename in filenames:
        count_words(filename)
#test5()

# 失败时一声不吭
# Python有一个pass 语句，可在代码块中使用它来让Python什么都不要做
def count_words2(fileName):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(fileName) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + fileName + " has about " + str(num_words) +" words.")

def test6():
    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
    for filename in filenames:
        count_words2(filename)
#test6()

