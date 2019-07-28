with open('./test', 'r', encoding='utf-8') as f:
    sum = 0
    count = 0
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if len(line) == 0:
            continue
        else:
            sum = sum + len(line)
            count = count + 1
print(round(sum / count))

