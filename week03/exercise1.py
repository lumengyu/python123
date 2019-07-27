a = int(input())
result = pow(a,0.5)
result = "{:.3f}".format(result)
if len(result) > 30:
    print(result)
else:
    length = len(result)
    padding = ""
    for i in range( 30 - length):
        padding = padding + "+"
    print(padding + result)