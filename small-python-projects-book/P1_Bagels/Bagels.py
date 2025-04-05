import random

tries = 10
number = str(random.randint(100,999))
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say: That means:")
print("   Pico      One digit is correct but in the wrong position.")
print("   Fermi      One digit is correct and in the right position.")
print("   Bagels      No digit is correct.")
print("I have thought up a number.\n You have 10 guesses to get it.")
while tries!=0:
    guess = str(input(f"Please input your guess : "))
    if guess==number:
        print(f"You win in {10-tries}")
    else:
        for i in range(len((guess))):
            if guess[i] in number:
                if number[i]==guess[i]:
                    print(f"{guess[i]} is Fermi")
                else:
                    print(f"{guess[i]} is Pico")
            else:
                print(f"{guess[i]} is Bagels")
        print(f"You have {tries} more")
    tries-=1
    if tries==0 or guess==number:
        print(f"the number was {number}")
