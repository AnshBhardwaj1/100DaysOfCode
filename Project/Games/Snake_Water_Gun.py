import random
score=0
round=1
def check (items,inp):
    ran=random.randint(0,2)
    global score
    cinp=items[ran]
    if cinp==inp:
        print (f"We both chose {inp}")
    elif inp==items[ran+1]:
        print (f"You Lost because I chose {cinp}")
        score=score-1
    elif inp==items[ran-1]:
        print (f"You Won because I chose {cinp}")
        score=score+1
    else:
        print("Kindly enter correct input-> snake,water,gun")
    print (f"Your score is {score}\n\n\n\n\n")



score=0
itemss=['water','gun','snake','water']
print("Press Q to exit")
while True:
    round+=1
    print(f"Round {round}. ")
    inpp=str(input("What do you choose : "))
    inpp=inpp.lower()
    if inpp=='q' or inpp== 'Q':
        exit()
    else:
        check(itemss,inpp)