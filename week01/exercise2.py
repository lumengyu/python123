TempStr = input()
TempStr_list = TempStr.split()
m = TempStr_list[0]
if m[0] == '-':
    m = -1 * float(m[1:])
else:
    m = float(TempStr_list[0])
op = TempStr_list[1]
n = TempStr_list[2]
if n[0] == '-':
    n = -1 * float(n[1:])
else:
    n = float(TempStr_list[2])
if op == '+':
    print("{:.2f}".format(m + n))
elif op == '-':
    print("{:.2f}".format(m - n))
elif op == '*':
    print("{:.2f}".format(m * n))
else:
    print("{:.2f}".format(m / n))
eval( '3 * x' )