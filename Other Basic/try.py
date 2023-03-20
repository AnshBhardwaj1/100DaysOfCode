lower_alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
final=[]
for i in lower_alphabet:
    for j in lower_alphabet:
       num=str(i)+str(j)
       final.append(num)
f=open("username.txt",'w')
for i in final:
    print (i," is done")
    f.writelines(f"{i}\n")
f.close()
