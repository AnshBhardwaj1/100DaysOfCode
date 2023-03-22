class Library:
    def __init__(self,book_id) -> None:
        self.id=book_id
    def count (self):
        return self.id
print ("Library already has following Books")

g=open('/home/ansh/Desktop/Python/Code/Project/Library Management/num.txt','r')
ID=g.read(1)
ID=int(ID)
g.close()
g=open('/home/ansh/Desktop/Python/Code/Project/Library Management/library.txt','r')
print(g.read())
g.close()
num_books=int(input("How many books do you have : "))
f=open("/home/ansh/Desktop/Python/Code/Project/Library Management/num.txt",'w')
f.writelines(f"{ID+num_books}")
f.close()
for i in range(num_books):
    f=open("/home/ansh/Desktop/Python/Code/Project/Library Management/library.txt",'a')
    name=input("what is name of your book : ")
    ID+=1
    f.writelines(f"{ID}. {name}\n")
    f.close()
g=open('/home/ansh/Desktop/Python/Code/Project/Library Management/library.txt','r')
print(g.read())
g.close()
