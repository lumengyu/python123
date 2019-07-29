import jieba

with open('沉默的羔羊.txt','r',encoding='utf-8')as f:
    txt = f.read()
    words = jieba.lcut(txt)
    count={}
    for i in words:
        if len(i) == 1:
            continue
        else:
            count[i] = count.get(i,0) + 1
list = list(count.items())
result = ""
max = 0
for k,v in count.items():
    if int(v) > max:
        max = int(v)
        result = k
print(result)