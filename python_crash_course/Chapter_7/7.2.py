# while 循环

def while1():
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1 # current_number = current_number + 1

def while2():
    prompt = "\nTell me something, and I will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program. "
    message = ""
    while message != 'quit':
        message = input(prompt)
        if message != 'quit':
            print(message)
#while2()

#  使用标志
def while3():
    prompt = "\nTell me something, and I will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program. "
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)
#while3()

# 使用break 退出循环
def bre():
    prompt = "\nPlease enter the name of a city you have visited:"
    prompt += "\n(Enter 'quit' when you are finished.) "
    while True:
        city = input(prompt)
        if city == 'quit':
            break
        else:
            print("I'd love to go to " + city.title() + "!")
#bre()

# 执行continue 语句，让Python忽略余下的代码，并返回到循环的开头
def odd():
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)
odd()








