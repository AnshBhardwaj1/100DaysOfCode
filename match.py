num1=int(input("Write your number"))
match num1 :
    case 1:
        print ("Your number is 111",num1)
    case 2:
        print ("Your number is222 ",num1)
    case 7:
        print ("Your number is 777 ",num1)
    case _ if (num1<10):
        print ("Your number is less than 10 and it is",num1)
    case _ if (num1>10):
        print ("Your number is greater than 10 and it is ", num1)