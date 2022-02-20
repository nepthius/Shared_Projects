ph  = True 
while(ph):
	Curr = input("What is your favorite sport? \n Basketball, MMA, Equestrian, or Skateboarding")
	if(Curr == 'b' or Curr == 'B'): 
		Chars[4]+=1
		ph = False
	elif(Curr[0]=='M' or Curr[0] == 'm'):
		Chars[0]+=1
		Chars[1]+=1
		Chars[2]+=1
		Chars[3]+=1
		ph = False
	elif(Curr==[0]'S' or Curr[0]=='s'): 
		Chars[7]+=1
		Chars[8]+=1
		ph = False
	elif(Curr==[0]'E' or Curr[0]=='e'):
		Chars[5]+=1
		Chars[6]+=1
		Chars[9]+=1
		ph = False
	else:
		print("That is not a valid option. Please Try Again")
ph  = True 
while(ph):
	Curr = input("What is your dream job? \n Doctor, Engineer, Astronaunt, Athlete")
	if(Curr[0] == 'D' or Curr[0] == 'd'): 
		Chars[5]+=1
        Chars[7]+=1
		ph = False
	elif(Curr[1]=='T' or Curr[1] == 't'):
		Chars[0]+=1
		Chars[1]+=1
		Chars[2]+=1
		Chars[3]+=1
        Chars[4]+=1
		ph = False
	elif(Curr[0]=='E' or Curr[0]=='e'): 
		Chars[6]+=1
		Chars[9]+=1
		ph = False
	elif(Curr[1]=='S' or Curr[1]=='s'):
		Chars[3]+=1
        ph = False
	else:
		print("That is not a valid option. Please Try Again")
ph  = True 
while(ph):
	Curr = input("Are you a night owl or an early bird?")
	if(Curr[0] == 'N' or Curr[0] == 'n'): 
		Chars[1]+=1
        Chars[5]+=1
        Chars[7]+=1
		ph = False
	elif(Curr[0]=='A' or Curr[0] == 'a'):
		Chars[2]+=1
		Chars[6]+=1
		ph = False
	else:
		print("That is not a valid option. Please Try Again")
ph  = True 
while(ph):
	Curr = input("Your friend is in a fight, what do you do? /n Break it up, Join the fight, Call for Help, Run Away")
	if(Curr[0] == 'B' or Curr[0] == 'b'): 
		Chars[1]+=1
        Chars[7]+=1
		ph = False
	elif(Curr[0]=='C' or Curr[0] == 'c'):
		Chars[5]+=1
		Chars[6]+=1
		Chars[9]+=1
		ph = False
	elif(Curr[0]=='J' or Curr[0]=='j'): 
		Chars[0]+=1
		Chars[2]+=1
		ph = False
	elif(Curr[0]=='R' or Curr[0]=='r'):
		Chars[3]+=1
        Chars[4]+=1
        Chars[8]+=1
        ph = False
	else:
		print("That is not a valid option. Please Try Again")h  = True 
while(ph):
	Curr = input("How often do you go out\n Never, Two to Three Times, Once, All the time ")
	if(Curr[0] == 'T' or Curr[0] == 't' or Curr[0]=='2'): 
		Chars[5]+=1
        Chars[7]+=1
		ph = False
	elif(Curr[0]=='N' or Curr[0] == 'n'):
		Chars[2]+=1
		Chars[6]+=1
		ph = False
	elif(Curr[0]=='O' or Curr[0]=='o'): 
		Chars[1]+=1
		Chars[8]+=1
        Chars[9]+=1
		ph = False
	elif(Curr[0]=='A' or Curr[0]=='a'):
		Chars[0]+=1
        Chars[3]+=1
        Chars[4]+=1
        ph = False
	else:
		print("That is not a valid option. Please Try Again")

