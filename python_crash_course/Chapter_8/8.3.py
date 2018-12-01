# 返回值
# 使用return 语句将值返回到调用函数的代码行

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

# 中间名是可选的，因此在函数定义中最后列出该形参，并将其默认值设置为空字符串
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    # Python将非空字符串解读为True
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
#print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
#print(musician)

# 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person
#print(build_person('jimi', 'hendrix'))

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
#print(build_person('jimi', 'hendrix', '22'))

# 结合使用函数和while 循环
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")

