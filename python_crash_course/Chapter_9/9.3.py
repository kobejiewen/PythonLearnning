# 继承,子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法

# 9.3.1 子类的方法__init__()
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# 创建子类时，父类必须包含在当前文件中，且位于子类前面
# 定义子类时，必须在括号内指定父类的名称
class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)  # super()要加括号
        """
        super() 是一个特殊函数，帮助Python将父类和子类关联起来。
        这行代码让Python调用ElectricCar 的父类的方法__init__(),
        让ElectricCar 实例包含父类的所有属性
        """
my_tesla=ElectricCar('tesla','modelX','2016')
print(my_tesla.get_descriptive_name())

# 给子类定义属性和方法
class NewCar(Car):
    def __init__(self,make,model,year):
        super().__init__(self,make,model,year)
        self.battery_size=70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

niuniu=NewCar('xiaoniu', 'X5', 2016)
print(niuniu.get_descriptive_name())
print(niuniu.describe_battery())

