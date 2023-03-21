def Greet (fx):
    def mfx(*args,**kwargs):
        print ("hello welcome to function")
        fx(*args,**kwargs)
        print ("thanks for using my function")
    return mfx
@Greet
def add (a,b):
    print (a+b)

def mlti(a,b):
    print (a*b)

print (Greet(mlti)(3,4))
add(5,3)