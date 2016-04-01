import random

random_card_number = (int)(random.random() * 52)

rank_number = random_card_number // 4

if rank_number == 0:
    rank = "Ace"
elif rank_number == 10:
    rank = "Jack"
elif rank_number == 11:
    rank = "Queen"
elif rank_number == 12:
    rank = "King"
else:
    rank = str(rank_number+1)
    
suit_number = random_card_number % 4

if suit_number == 0:
    suit = "Clubs"
elif suit_number == 1:
    suit = "Diamonds" 
elif suit_number == 2:
    suit = "Hearts" 
elif suit_number == 3:
    suit = "Spades" 

print("Random card number is: ",random_card_number)
print("The card got picked is: ",rank,"  of ",suit)