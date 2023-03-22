import string
def decrypt(str):
    lower = list(string.ascii_lowercase)
    str_list=str.split(" ")
    for i in str_list:
        i=list(i)
        word=i[3:-3]
        word.insert(0,word[-1])
        word.pop(-1)
        print(*word,sep='',end=' ')
    return ''
if __name__=="__main__":
    og_str=input("What do you want to encrypt : ")
    decrypt(og_str)