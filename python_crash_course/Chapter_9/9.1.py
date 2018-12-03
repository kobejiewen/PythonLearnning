# 类
# 创建和使用类

# 在Python中，首字母大写的名称指的是类
class Dog():
    """
    一次模拟小狗的简单尝试
    """
    def __init__(self,name,age): #Python调用这个__init__() 方法来创建Dog 实例时，将自动传入实参self
        """初始化属性name和age"""
        self.name=name  #以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量'
        self.age=age    #像这样可通过实例访问的变量称为属性
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over!")

# 根据类创建实例
# 一般小写指的是根据类创建的实例my_dog
my_dog=Dog('dudu',7) #方法__init__() 并未显式地包含return 语句，但Python自动返回一个表示这条小狗的实例
# 访问属性
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# 调用方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('lucy', 3)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()