############### Blackjack Project #####################
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
end_game = False
x = 0
user_cards = []
computer_cards = []

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2: 
# FIXME: len(cards) is returning 3 intead of 2, which throws an Exception has occurred: TypeError unsupported operand type(s) for +: 'int' and 'function'
        return 0  # 0 represents a blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())         

while end_game == False: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are {user_cards} with a score of {user_score}\n")
    print(f"Computer's first card: {computer_cards[0]}\n")

    if user_score == 0 or user_score > 21 or computer_score == 0:
        end_game = True
    else: 
        continue_prompt = input("Would you like to draw another card? 'y' or 'n': ")
        if continue_prompt == 'y':
            user_cards.append(deal_card)
            calculate_score(user_cards)
        else: 
            end_game = True
        