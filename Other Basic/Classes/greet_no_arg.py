def greet (fx):
    def mfx():
        print ("hello kya haal chaal")
        fx()
        print("okiee byee")
    return mfx()

def nello():
    print ("nello")

greet(nello)

@greet
def hello():
    print ("helo kaise ho")

hello