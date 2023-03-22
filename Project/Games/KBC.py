import random
bal=0
i=0
questions=['what is my name','whhat is my age']
opt_a=['andh','15']
opt_b=['bhand','18']
opt_c=['sand','17']
opt_d=['ansh','16']
solu=['d','b']
while bal>=0:
    i+=1
    ran=random.randint(0,1)
    print (i,". ",questions[ran], " ? ")
    print ("A.) ",opt_a[ran])
    print ("B.) ",opt_b[ran])
    print ("C.) ",opt_c[ran])
    print ("D.) ",opt_d[ran])
    ans=input("Your answer is : ")
    ans=ans.lower()
    print (ans)
    if ans==solu[ran]:
        print ("Your answer is correct and you win 10000 rupees")
        bal+=10000
        print ("Your new balance is ",bal)
    else :
        print ("Yoyr answer was wrong")
        print ("Thanks for playing")
        print ("Your final winning amount was", bal)
        break



