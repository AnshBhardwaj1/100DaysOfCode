import random
def encrypt(og_str):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #og_str=input("What do you want to encrypt : ")
    og_str=og_str.lower()
    inp_str_list=og_str.split(" ")
    encrpted=[]
    for i in range(len(inp_str_list)):#now the following is done for a word
        og=[]
        og=list(inp_str_list[i])#converting everyword to a list, where og is the list of each word, like if
        #print (og)             #word is ansh then  og = ['a','b','c','d']
        og.insert(len(og),og[0])#we are taking the first letter of the word to end
        og.pop(0)#removing first letter afterwards
        for m in range(3):#to add 3 random letters in front and back of each word
            ran=random.randint(0,25)
            og.append(alphabet[ran])
            og.insert(0,alphabet[(25-ran)])
        og.append(" ")#adding "" " to end of the word jisse aaram se sentence ban jae
        for j in range(0,len(og)):
            print(og[j], end="")#ab jo list aise ansh ki ['n','s','h','a',' '] ban chuki hai, uske ek ek 
                                #element ko print karva raha hu, with end ='', such thatvo agli agli line 
                                #main print hone ki jagah ke saath print ho jae
if __name__=="__main__":
    og_str=input("What do you want to encrypt : ")
    encrypt(og_str)