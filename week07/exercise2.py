with open('./data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    nlines = []
    for i in lines[::-1]:
        nlines.append(i)
    for row in nlines:
        tempstr = ""
        row = row.replace("\n","")
        col = row.split(",")
        for item in col[::-1]:
            tempstr = tempstr + item + ";"
        tempstr = tempstr[:-1]
        print(tempstr)

#Correct Answer:
'''lines = f.readlines()
lines.reverse()

for line in lines:
    line = line.replace('\n','')
    t = line.split(",")

for line in lines:
    line = line.replace('\n','')
    line =line.replace(' ','')
    t = line.split(",")
    t.reverse()
    print(";".join(t)) '''

