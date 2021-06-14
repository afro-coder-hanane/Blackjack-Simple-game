############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
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