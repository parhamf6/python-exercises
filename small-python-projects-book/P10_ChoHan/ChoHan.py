import random

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

mon = 5000
sta = 1
while sta!=0:
    bet = int(input(f"You Have {mon} How much do you want to bet ? (or Quit : 0) : "))
    if bet==0:
        sta = 0
        print(f"good lock you money is {mon}")
    else:
        print("roliing dices")
        ans = int(input("Cho (even) : 2 OR Han (odd) : 1 :"))
        d1 = random.choice(dice1)
        d2 = random.choice(dice1)
        if (d1+d2)%2==0:
            if ans==2:
                print(f"you won {bet*2}")
                print(f"house fee is {(bet*2)/10}")
                mon = mon + ((bet*2)-int((bet*2)/10))
            else:
                print(f"you lose {bet}")
                mon = mon - bet
        elif (d1+d2)%2!=0:
            if ans==1:
                print(f"you won {bet*2}")
                print(f"house fee is {(bet*2)/10}")
                mon = mon + ((bet*2)-int((bet*2)/10))
            else:
                print(f"you lose {bet}")
                mon = mon - bet
        print(f"the sum of dices was {d1+d2}")
        print(f"your amount of money is {mon}")