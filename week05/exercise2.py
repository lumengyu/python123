def prime(m):
    if(m <= 1):
        return False
    for j in range(2, m):
        if m % j == 0 and m != j:
            return False
    return True

n = eval(input())
if not isinstance(n , int):
    n = int(n) + 1
else:
    n = n + 1
count = 0
result = ""
while count <= 4:
    if(prime(n)):
        result = result + str(n)
        count = count + 1
        if count != 5:
            result = result + ","
    n = n + 1
print(result)