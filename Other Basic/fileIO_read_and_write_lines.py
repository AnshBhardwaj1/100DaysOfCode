f = open('Other Basic/txttt.txt', 'r')
#while True:#
    #line = f.readline()
    #if not line:#this is the boolean way to do that, you can also do is len(line.strip()==0:)
    #print (line.strip())
    #print (str(line.strip("")))    
    #if (len(line.strip())==1) :#or (len(line.strip())==0):
    #    break
    #print(line,end="")
f.close()
write=open('Other Basic/NewTxt.txt','w')
lin=[i for i in range(5)]
for j in range(len(lin)):
    write.writelines(str(lin[j]))
write.close()