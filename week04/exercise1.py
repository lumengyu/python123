for i in range(1000,9999):
    temp = str(i)
    sum = pow(int(temp[0]),4) + pow(int(temp[1]),4) + pow(int(temp[2]),4) + pow(int(temp[3]),4)
    if sum == i:
        print(i)