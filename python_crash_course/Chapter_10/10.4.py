# 存储数据

# 使用模块json来存储数据
import  json

def test1():
    numbers = [2,3,5,7,11,13]
    filename = 'numbers.json'

    # 函数json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象
    with open(filename,'w') as f_obj:
        json.dump(numbers,f_obj)

    # json.load() 将这个列表读取到内存中
    with open(filename) as f_obj:
        numberList = json.load(f_obj)
    print(numberList)
#test1()

# 保存和读取用户生成的数据
def test2():
    username = input("What is your name? ")
    file = 'username.json'
    with open(file, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")

    with open(file) as f_obj:
        name = json.load(f_obj)
        print("Welcom back, " + name + "!")
#test2()

def test3():
    # 如果以前存储了用户名，就加载它
    # 否则，就提示用户输入用户名并存储它
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

#test3()

# 重构
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()

