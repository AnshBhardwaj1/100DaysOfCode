def fibo (n):
    if (n==1 ):
        return 1
    elif (n==0):
        return 0
    else :
        return (int(fibo(n-1) + int(fibo(n-2))))
for i in range (0,10):
    print (fibo(i), end=" , ")