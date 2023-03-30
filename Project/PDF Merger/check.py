if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
mega=[[0,0,0]]
for i in range(x+1):
    smoll=[0,0,0]
    smoll[0]=i
    for j in range(y+1):
        smoll[1]=y
        for k in range(z+1):
            smoll[1]=z
            mega.append(smoll)
print (mega)
print(len(mega))
for smool in mega:
    print (smool)
    if smool[0]+smool[1]+smool[2]==n:
        mega.remove(smool)
print (mega)