# 使用if 语句处理列表

requested_toppings = [] # 列表为空时返回False
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")
else:
    print("requested_topping is null")

