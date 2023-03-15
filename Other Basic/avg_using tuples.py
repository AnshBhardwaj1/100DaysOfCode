def avgg (*numbers):
    sum=0
    tot=0
    for i in numbers :
        #print (type(i))
        for j in i :
            tot+=1
            sum=sum+j
    return (sum/tot)
nn=(1,2,3,4,5,6,7,8,9,10)
print (avgg(nn))

def avggg(*nuumbers):
    summ=0
    for i in nuumbers :
        summ+=i
    print (summ/len(nuumbers))
avggg(5,6,9,8,7,4,5,6,9,8)