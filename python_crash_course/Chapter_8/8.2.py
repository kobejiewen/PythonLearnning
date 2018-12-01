# 传递实参

# 8.2.1　位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet('hamster', 'harry')
#describe_pet('布偶','可乐')

# 8.2.2　关键字实参,避免传参顺序错误
def describe_pet2(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet2(animal_type='hamster', pet_name='harry')
#describe_pet2(pet_name='可乐',animal_type='布偶')

# 可给每个形参指定默认值
def describe_pet3(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet3(pet_name='haha')
#describe_pet3('dudu')

# 等效的函数调用

# 避免实参错误
