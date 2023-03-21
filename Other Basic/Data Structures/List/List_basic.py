l=[3,4,5,'hello',9]
for i in l:
    print (i , end=' ')
#print (l[-0])
for i in range (0, len(l)):
    if (l[i]==9):
        print (l[i], " is there at ", i+1)
    else :
        continue #pass

if int("9") in l : # 9 will be true '9' will not be true since string main 9 nahi hai
    #par integer hai isliye ya to seedha 9 milega ya fir int("9")
    print ("9 is there")
else :
    print ("9 is not there")
print (l[:4])
print (l[1:3:2])
lst=[i for i in range(0,4)]
print (lst)
lst = [k for k in l[3]]
print (lst)
nl=['ansh','rohan','hello','kalu']
lst=[ i for i in nl if True ]#'o' in i] the later gives naems with o in it
print (lst)