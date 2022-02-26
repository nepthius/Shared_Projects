import random
a = True
while(a):
    x = input("Rock, Paper or Scissors?") 
    y = random.randint(1,3)
    if(x[0]=='R' or x[0]=='r' ):
        x = 1
    elif(x[0]=='P' or x[0]=='p'):
        x=2
    else: 
        x=3
    if(y==1):
        print("Computer Chose Rock!")
    elif(y==2):
        print("Computer Chose Paper!")
    else: 
        print("Computer Chose Scissors!")

    if(x+1==y or (x==3 and y==1)): 
        print("Sorry you lose! Continue? (Y/N)")
        tempt = input()
        if(temp[0] == 'N' or temp[0]=='n'):
            a = False
    elif(y+1==x or (y==3 and x==1)):
        print("You win! Continue? (Y/N)")
        temp = input()
        if(temp[0] == 'N' or temp[0]=='n'):
            a = False
    else:
        print("Tie try again")
            

