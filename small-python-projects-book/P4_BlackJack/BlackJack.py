import random

suits = ['h', 'd', 's', 'c']  # hearts, diamonds, spades, clubs
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']  # card ranks

deck = [rank + suit for suit in suits for rank in ranks]
money = 5000
stat = 1
while stat!=0:
    dealer = []
    player = []
    for d in range(2):
        de = random.choice(deck)
        dealer.append(de)
        
