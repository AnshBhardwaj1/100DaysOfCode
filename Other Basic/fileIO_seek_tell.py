with open("Other Basic/txttt.txt",'r') as f:
    f.seek(10)
    print (f.read(10))
    f.seek(14)
    print(f.read(9))
    print(f.tell())
