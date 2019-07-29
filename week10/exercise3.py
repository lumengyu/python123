temp = eval(input())
if isinstance(temp,dict):
    inverse_dic = {}
    for key, val in temp.items():
        inverse_dic[val] = key
    print(inverse_dic)
else:
    print("输入错误")