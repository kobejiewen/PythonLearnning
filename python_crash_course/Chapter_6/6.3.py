# 遍历字典

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# 方法items()它返回一个键—值对列表，即便遍历字典时，键—值对的返回顺序也与存储顺序不同
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 遍历字典中的所有键 keys()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print("name is "+name)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages:
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# 方法keys() 并非只能用于遍历,实际上,它返回一个列表，其中包含字典中的所有键
if 'bob'not in favorite_languages.keys():
    print("bob is not in")

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title())

# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language)

# 集合set类似于列表，但每个元素都必须是独一无二的
for language in set(favorite_languages.values()):
    print(language)

