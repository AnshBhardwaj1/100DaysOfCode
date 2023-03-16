import random
bal,i=0,0
questions=['what is my name ? ','what is my age ?','which language is this ?']
opt=[['andh','bhand','sand','ansh'],['15','18','19','73'],['c++','c','python','java']]
solu=['d','b','c']
q_done=[]
while bal>=0:
    if len(q_done)==len(questions):
        print ("We only have these many questions as of now")
        print ("Thanks for playing")
        break
    else :
        ran=random.randint(0,len(questions)-1)
        while ran in q_done :
            ran=random.randint(0,len(questions)-1)
        else :
            q_done.append(ran)
            i+=1
            print (i,". ",questions[ran], " ? ")
            opt2=opt[ran]
            print ("A. ",opt2[0],"\nB. ",opt2[1],'\nC. ',opt2[2],'\nD. ',opt2[3])
            ans=input("Your answer is : ")
            ans=ans.lower()
            if ans==solu[ran]:
                print ("Your answer is correct and you win 1000 rupees")
                bal+=1000
                print ("Your new balance is ",bal)
            else :
                print ("Yoyr answer was wrong")
                print ("Thanks for playing")
                print ("Your final winning amount was", bal)
                break