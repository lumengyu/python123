TempStr = input()
baseStr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
for i in TempStr:
    if i in baseStr:
        result = result + i
print(result)