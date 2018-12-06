# 测试类

# 各种断言方法
"""
    assertEqual(a, b)               核实a == b
    assertNotEqual(a, b)            核实a != b
    assertTrue(x)                   核实x 为True
    assertFalse(x)                  核实x 为False
    assertIn(item , list )          核实 item 在 list 中
    assertNotIn(item , list )       核实 item 不在 list 中
"""

# 一个要测试的类

from python_crash_course.Chapter_11.survey import AnonymousSurvey
#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
def test1():
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    #显示问题并存储答案
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.store_response(response)
    # 显示调查结果
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()
#test1()

# 测试AnonymousSurvey 类
"""使用方法assertIn() 来核实它包含在答案列表中"""
import  unittest
from python_crash_course.Chapter_11.survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarish']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)

#unittest.main()

# 方法setUp()
"""
如果你在TestCase 类中包含了方法setUp() ， Python将先运行它，再运行各个以test_打头的方法。
在你编写的每个测试方法中都可使用在方法setUp() 中创建的对象了。
"""
class TestAnonymousSurvey2(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
unittest.main()

