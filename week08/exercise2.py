init = input()
temp = eval(init)
if isinstance(temp, int) and init.isdigit():
    print(pow(temp,2))
elif isinstance(temp, float):
    print(pow(temp,2))
elif isinstance(temp,complex):
    print(pow(temp,2))
else:
    print("输入有误")