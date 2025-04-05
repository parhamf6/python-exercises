import random

# crate random bag creating function
marble_bag = ["r","r","r","r","g","g","g","g","g","g"]


# create random replacing function
money = 1000
game = 1
while game==1:
    bet = int(input("Chose amount of your bet please : "))
    bag_index = random.randint(0,9)
    chosen = marble_bag[bag_index]
    if chosen=="r":
        money-=bet
        print("You Lose its Red")
    elif chosen=="g":
        money+=bet
        print("you Win its Green")
    print(f"Your Money : {money}")
    if money<500:
        game = 0
        break
    continue_game = str(input("Another Round ? yes(y) OR no(n) :"))
    if continue_game=="n":
        game = 0
        print("Good Luck")
        break
