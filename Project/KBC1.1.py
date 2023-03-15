import random
bal=0
i=0
questions=['what is my name ? ','what is my age ?','which language is this ?']
opt=[['andh','bhand','sand','ansh'],['15','18','19','73'],['c++','c','python','java']]
solu=['d','b','c']
q_list=[i for i in range(0,len(questions))]
while bal>=0:
    if len(q_list)==0:
        print ("We only have these many questions as of now")
        print ("Thanks for playing")
        break
    else :
        i+=1
        #print (q_list)
        ran1=random.randint(0,len(q_list)-1)
        ran=q_list[ran1]
        pp=q_list.index(ran)
        q_list.pop(pp)
        print (i,". ",questions[ran], " ? ")
        opt2=opt[ran]
        print ("A. ",opt2[0],"\nB. ",opt2[1],'\nC. ',opt2[2],'\nD. ',opt2[3])
        ans=input("Your answer is : ")
        ans=ans.lower()
        #print (ans)
        if ans==solu[ran]:
            print ("Your answer is correct and you win 1000 rupees")
            bal+=1000
            print ("Your new balance is ",bal)
        else :
            print ("Yoyr answer was wrong")
            print ("Thanks for playing")
            print ("Your final winning amount was", bal)
            break



