# Python标准库

# 要创建字典并记录其中的键—值对的添加顺序，可使用模块collections 中的OrderedDict类

from collections import OrderedDict # 创建OrderedDict类的一个实例
favorite_languages=OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

