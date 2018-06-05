filename = "filenet.flg"
with open(filename, 'r', encoding='utf-8') as f:
    txt = f.readlines()
    print(type(txt))
    print(len(txt))
    print(txt[1])