from cnblogs.StartUp import SecondTest

def load():
    St=SecondTest("load other")
    St.SayFrist()
    St.SaySecond()

# print(complex(1))
# print(complex(4,5))
# print(complex('3+9j'))

def out():
    dan='m1n9'
    print("dan:  {0}".format(dan))
    dan1='Our "young"!'
    print("dan1:  {0}".format(dan1))
    dan2='''Our
    young
    cool'''
    print("dan2:  {0}".format(dan2))
    dan3="""Our
    young
    cool"""
    print("dan3:  {0}".format(dan3))
    dan4="m1n9 'dad' asd"
    print("dan:  {0}".format(dan4))

    comment='I\'m young'
    print(comment)
    description="Our \nyoung"
    print(description)

    comment=r'Our \nyoung'
    print(comment)
    description="Our \nyoung"
    print(description)
    three="Our young\n"*3
    print(three)

def subStr():
    description="ABCDEFGHIJK"
    d1=description[0]
    print("d1:   {0}".format(d1))
    d2=description[8]
    print("d2:   {0}".format(d2))
    d3=description[:3]
    print("d3:   {0}".format(d3))
    d4=description[3:]
    print("d4:   {0}".format(d4))
    d5=description[3:6]
    print("d5:   {0}".format(d5))

# load()
# out()
# subStr()

def dataType():
    # 列表
    people = ["刘一", "陈二", "张三", "李四", "王五", "赵六", "孙七", "周八", "吴九"]
    print (people[3])
    # 元组
    names = ("刘一", "陈二", "张三", "李四", "王五", "赵六", "孙七", "周八", "吴九")
    print (names[1])
    # 集合
    xitems = set("1222234566666789")
    xitems.add("x")
    xitems.remove("8")
    xitems.discard("80")
    print (xitems)
    yitems = set("1357")
    # 交集
    print("交集:{0}".format(xitems & yitems))  # xitems&yitems = xitems.intersection(yitems)
    # 并集
    print("并集:{0}".format(xitems | yitems))  # xitems|yitems = xitems.union(yitems)
    # 差集
    print("差集:{0}".format(xitems - yitems))  # xitems-yitems = xitems.difference(yitems)
    xitems.pop()
    xitems.clear()
    print("xitems集合被清空:{0}".format(xitems))
    # 字典
    dictionary = {'name': 'toutou', "age": "26", "sex": "male"}
    print(dictionary["name"])
    # 向字典中添加项目
    dictionary['hobby'] = 'cnblogs'
    print("sex {0}".format(dictionary["sex"]))
    print("hobby {0}".format(dictionary["hobby"]))

dataType()
