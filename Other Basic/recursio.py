def fact (n):
    pro=1
    if (n==1 or n==0):
        return 1
    else :
        return (n*fact(n-1))
nu=int(input("write your number : "))
print (fact(nu))