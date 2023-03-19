#f=open("Other Basic/txttt.txt",'w')
#f.write("hello i am ansh    m")
#f.close()
#g=open("Other Basic/txttt.txt",'r')
#text=g.read()
##print (text)
#g.close()
#
f = open('Other Basic/txttt.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
#while True:
 #   line = f.readline()
  #  #if not line:#this is the boolean way to do that, you can also do is len(line.strip()==0:)
   # if (len(line.strip())==1) or (len(line.strip())==0):
    ##rint(line,end="")