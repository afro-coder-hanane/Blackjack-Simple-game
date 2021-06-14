
import random
from replit import clear
from art import logo

print(logo)

"""variables"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player=[]
computer = []
"""functions"""
def random_number():
    return (random.choice(cards))
def initialize(lst):
  for x in range(2):
    draw(lst) 
   
def display():
  print (f"your cards are {player}, Score: {sum(player)}")

def display_first():
   print(f"computer first card: {computer[0]}")  

def is_bust(lst):
  if sum(lst)>21:
    return True

def is_smaller(lst):
  if(sum(lst)<17):
    return True

def draw(lst):
  if (random_number()==11 and sum(lst)>21):
    lst.append(1)
  else:
    lst.append(random_number())

def is_over(lst=player, lst1=computer):
  if(sum(lst)>21):
      print("player lost")
      return False
  else:
      print("computer lost")
      return False

def compare(lst1,lst2):
   sum1=sum(lst1)
   sum2=sum(lst2)
   if(sum1>sum2 ):
     print(f"{sum1} is greater than {sum2}, user won")
   elif(sum1<sum2 ):
     print(f"{sum2} is greater than {sum1}, computer won")
   else:
     print("No winner, it is a draw")

   


def blackjack():
  initialize(player)
  initialize(computer)  
  display()
  display_first()
  
  if(is_bust(player)):
    print("It is a bust, computer won")
  elif(is_bust(computer)):
    print("It is a bust, player won")
  elif(sum(computer)==21):
    print(f"Computer cards are{computer}, final score is {sum(computer)}")
    print("Blackjack, computer won")
  elif(sum(player)==21):
    print("Blackjack, player won")
  else:
    should_continue = True  
    while(should_continue):
      draw_choice = input("type'y' to get another card and 'n' to pass\n").lower()
      if draw_choice == 'y':
        draw(player)
        display()
        display_first()
        if(sum(player)>21):
          print(f"Computer cards are{computer}, final score is {sum(computer)}")
          print("player lost")
          should_continue= False
        # should_continue = is_over(player, computer) 
      else:
        print(f"Your cards are{player}, final score is {sum(player)} \n")
        
        if sum(computer)<17:
          while(sum(computer)<17 and should_continue==True):
            draw(computer)
            if(sum(computer)>21):
              print("computer lost")
              should_continue= False
            # should_continue = is_over(player, computer)
           
        print(f"Computer cards are{computer}, final score is {sum(computer)}")
        """compare"""
        compare(player, computer)
        should_continue = False
  play_again= input("type 'y' to play again and any key to stop\n").lower() 
  if (play_again=='y'):
    player.clear()
    computer.clear()
    blackjack()
  
if(input("press 'y' to start\n").lower()=='y'):
  blackjack()
else:
  clear()  