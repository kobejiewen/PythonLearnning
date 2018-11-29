'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

name="ada lovelace"
print(name.title())

name="Ada Lovelace"
print(name.upper())
print(name.lower())

first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print(full_name)
print("Hello,"+full_name.title()+"!")

#字符串中添加制表符，可使用字符组合\t
print("\tPython")
#字符串中添加换行符，可使用字符组合\n
print("Languages:\nPython\nJavaScript")
print("Languages:\n\tPython\n\tJavaScript")

favorite_language="   Python    "
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language.rstrip())

