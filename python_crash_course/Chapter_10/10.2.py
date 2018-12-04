# 写入文件

# 写入空文件
"""
    读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）.
    如果你省略了模式实参， Python将以默认的只读模式打开文件。
"""
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming")
# ! ! ! 以写入（'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在， Python将在返回文件对象前清空该文件
# ! ! ! 注意 Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str() 将其转换为字符串格式

# 写入多行,\n 换行
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件，给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文件。
# Python不会在返回文件对象前清空文件
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

