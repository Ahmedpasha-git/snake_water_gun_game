import random
l=["snake","water","gun"]
while True:
  you=input("Enter snake, water, gun:").lower()
  if you not in l:
    
    print("Invalid")
  else:
    
    you=l.index(you)
    computer=random.randint(0,2)
    print("you choose:",l[you])
    print("computer chhose:",l[computer])
    if you==0 and computer==1:
      print("you win!")
    elif you==1 and computer==2:
      print("you win!")
    elif you==2 and computer==0:
      print("you win!")
    elif you==computer:
      print("Its draw!")
    elif you==0 and computer==2:
      print("you lose!")
    elif you==1 and computer==0:
      print("you lose!")
    elif you==2 and computer==1:
      print("you lose!")
  again=input("do you want to play again!(yes/no):").lower()
  if again!="yes":
    break