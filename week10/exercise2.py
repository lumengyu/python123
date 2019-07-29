with open('test', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    s = set([])
    for l in lines:
        l = l.replace("\n","")
        s.add(l)
    print("共{:}关键行".format(len(s)))