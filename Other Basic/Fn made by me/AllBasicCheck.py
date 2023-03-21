import AllBasic
#print (lower_alphabet)
#print (upper_alphabet)
lis=list('hello my name is ansh')
#lis=[11,22,33,44,55,66,77,88,99]
AllBasic.print_list_sep(lis)
#The following has the lists which ,ay be required in any programme
lower_alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if __name__=="__main__":
    print("hello welcome to All Basic this contains all basic and important lists and functions")
    print("written by Ansh Bhardwaj, all the information of the functions are wriiten in # which")
    print("are present above the function, its example of sue is given below")
    #this hello will only be printed when we run this file but when we'll import it somewhere
    #hello print nahi hoga
    #otherwise hum agar if __name__=="__main__" nahi lagate to import AllBasic karte hi output main
    #hello aa jata

#FUCNTIONS START NOW
#1...........................................................................................
#print_list_sep is a function which takes two arguments , first is the list and second is the
#character you need between consecutive elements of the list
#can be directly written like 
#print_list_sep 
#OR
#print(print_list_sep) 
#both of them will work
def print_list_sep(print_list,seperatio=' '):
    for element_list_sep in print_list:
        print (element_list_sep,end=seperatio)
    return ""
#pis=[11,22,33,44,55,66,77,88,99]
#print(print_list_sep(pis," "))

#2...........................................................................................