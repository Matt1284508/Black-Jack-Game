############### Blackjack Project #####################
import random
from logo import logo
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
        
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0 # 0 represents a blackjack
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "\n   You went over. You lost!"

  if user_score == computer_score:
    return "\n   Draw"
  elif computer_score == 0:
    return "\n   You lost! Computer has Blackjack 🂡 🃞"
  elif user_score == 0:
    return "\n   You win with a Blackjack 🂡 🃞"
  elif user_score > 21:
    return "\n   You went over. You lost! 🂠 🂠"
  elif computer_score > 21:
    return "\n   ♦ Computer went over. You won! ♦"
  elif user_score > computer_score:
    return "\n   ♢ You won! ♢"
  else:
    return "\n   You lost!"

def play_game():        
    end_game = False
    user_cards = []
    computer_cards = []
    
    print(logo)     
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card()) 
    
    while end_game == False: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n Your cards are {user_cards} with a score of {user_score}")
        print(f"\n Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            end_game = True
        else: 
            continue_prompt = input("Would you like to draw another card? 'y' or 'n': ")
            if continue_prompt == 'y':
                user_cards.append(deal_card())
            else: 
                end_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n   Your final hand: {user_cards} | Final Score: {user_score}")
    print(f"   Computer's final hand: {computer_cards} | Final Score: {computer_score}")
    print(compare(user_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()