
def test01():
    socre=90
    if socre>=90:
        print("great")
    elif socre>=80:
        print("good")
    elif socre >=60:
        print("ok")

def test02():
    for i in range(0,3):
        print(i)
        print("index {0} {1}".format(i,"第一种打印"))
        print(f"index {i} {'第二种打印'}")
        print("index %d %s" % (i,"第三种打印"))
    print("end")

def Hello():
    print("Hello World")

def GetMax(x,y):
    if x>y:
        return x
    else:
        return y

#test01()
#test02()
#Hello()
#print(GetMax(10,6))

class FirstTest:
    def __init__(self,name):
        self._name=name
    def SayFrist(self):
        print("Hello {0}".format(self._name))
#F=FirstTest("wwj")
#F.SayFrist()

class SecondTest(FirstTest):
    def __init__(self,name):
        FirstTest.__init__(self,name)
    def SaySecond(self):
        print("good {0}".format(self._name))

# S=SecondTest("two")
# S.SayFrist()
# S.SaySecond()