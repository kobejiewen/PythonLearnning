# 使用类和实例

# car类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, brand, model, year):
        """初始化描述汽车的属性"""
        self.brand = brand
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.brand + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


# 给属性指定默认值
class Car2():
    """一次模拟汽车的简单尝试"""

    def __init__(self, brand, model, year):
        """初始化描述汽车的属性"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 200  # 创建一个名为odometer_reading 的属性，并将其初始值设置为0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.brand + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car2 = Car2('audi', 'a5', '2018')
print(my_new_car2.get_descriptive_name())
print(my_new_car2.read_odometer())

# 修改属性的值
# 1. 直接修改属性的值
car3 = Car2('audi', 'a8l', '2016')
print(car3.get_descriptive_name())
car3.odometer_reading = 230
print(car3.read_odometer())

# 2. 通过方法修改属性的值
car4 = Car2('audi', 's6', '2019')
print(car4.get_descriptive_name())
car4.update_odometer(210)
print(car4.read_odometer())

# 3. 通过方法对属性的值进行递增
car5 = Car2('subaru', 'outback', 2013)
print(car5.get_descriptive_name())
car5.increment_odometer(1000)
car5.read_odometer()
