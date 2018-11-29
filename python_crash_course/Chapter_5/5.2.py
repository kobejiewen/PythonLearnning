# 条件测试

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age_0 = 22
age_1 = 18
if (age_0>=21) and (age_1<=22) :
    print("ok")
if (age_0>=21) or (age_1<=2) :
    print("ok")

# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if  'mushrooms' in requested_topping:
    print("mushrooms is in")
if 'test' not in requested_topping:
    print("test not in")

# 布尔表达式
game_active = True
can_edit = False


