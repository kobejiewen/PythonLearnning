# 导入类

from python_crash_course.Chapter_9.car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

from python_crash_course.Chapter_9.car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# 导入整个模块
import python_crash_course.Chapter_9.car


# 导入模块中的所有类
from python_crash_course.Chapter_9.car import *

# 在一个模块中导入另一个模块

