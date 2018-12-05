# 测试代码
# 测试函数

from python_crash_course.Chapter_11.name_function import get_formatted_name

def test1():
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        last = input("Please give me a last name: ")
        if last == 'q':
            break
        formatted_name = get_formatted_name(first,last)
        print("\tNeatly formatted name: " + formatted_name + '.')

# 单元测试和测试用例
"""
    Python标准库中的模块unittest 提供了代码测试工具。单元测试 用于核实函数的某个方面没有问题；
    测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
    全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
"""

# 可通过的测试，以及不可通过的测试
import  unittest

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    # 所有以test 打头的方法都将自动运行
    def test_name(self):
        formatted_name = get_formatted_name('janis','joplin',)
        self.assertEqual(formatted_name,'Janis Joplin') # 断言方法
    def test_middle_name(self):
        formatted_name = get_formatted_name('janis','joplin','kobe')
        self.assertEqual(formatted_name,'Janis Kobe Joplin')

unittest.main()

# 添加新测试

