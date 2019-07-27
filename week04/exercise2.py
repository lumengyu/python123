sum = 0
for i in range(2, 101):
    for j in range(2, i+1):
        if j == i:
            sum = sum + i
        temp = i % j
        if temp == 0:
            break
print(sum)