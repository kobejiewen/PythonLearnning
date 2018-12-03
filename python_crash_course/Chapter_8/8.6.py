# 将函数存储在模块中
# 模块是扩展名为.py的文件

# 导入整个模块
import python_crash_course.Chapter_8.pizza
python_crash_course.Chapter_8.pizza.make_pizza(1, 'pepperoni')
python_crash_course.Chapter_8.pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定的函数  from module_name import function_name
from python_crash_course.Chapter_8.pizza import make_pizza
make_pizza(3,'pepperoni')
make_pizza(4, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as 给函数指定别名
from python_crash_course.Chapter_8.pizza import make_pizza as mp
mp(5,'pepperoni')
mp(6, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as 给模块指定别名
import python_crash_course.Chapter_8.pizza as p
p.make_pizza(7,'pepperoni')

# 导入模块中的所有函数 (*)
from python_crash_course.Chapter_8.pizza import *
make_pizza(8,'pepperoni')
make_pizza(9, 'mushrooms', 'green peppers', 'extra cheese')