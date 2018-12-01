# 使用while 循环来处理列表和字典

# 要在遍历列表的同时对其进行修改，可使用while 循环

# 在列表之间移动元素
def test1():
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
            print(confirmed_user.title())

# 删除包含特定值的所有列表元素
def test2():
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)
#test2()

# 使用用户输入来填充字典
def test3():
    responses = {}
    # 设置一个标志，指出调查是否继续
    polling_active = True
    while polling_active:
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")
        responses[name] = response
        # 看看是否还有人要参与调查
        repeat = input("Would you like to let another person respond? (yes/ no) ")
        if repeat == 'no':
            polling_active = False
    # 输出字典
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")
test3()