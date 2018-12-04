# 从文件中读取数据

# 要使用文本文件中的信息，首先需要将信息读取到内存中
# 读取整个文件

# 关键字with在不再需要访问文件后将其关闭,你只管打开文件，并在需要时使用它， Python自会在合适的时候自动将其关闭。
with open('pi_digits.txt') as file_object:  # 函数open() 返回一个表示文件的对象
    contents = file_object.read()  # read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行
    print(contents.rstrip())

# 逐行读取
filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
filename='pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    # 方法readlines()从文件中读取每一行，并将其存储在一个列表中；该列表被存储到变量lines中；在with代码块外,我们依然可以使用这个变量
for line in lines:
    print(line.rstrip())

# 使用文件的内容
filename='pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi = ''
for line in lines:
    pi += line.strip()
print('pi=' + pi)

# 包含一百万位的大型文件,只要系统的内存足够多，你想处理多少数据都可以
print('pi前20位=' + pi[:20])

# 圆周率值中包含你的生日吗
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

