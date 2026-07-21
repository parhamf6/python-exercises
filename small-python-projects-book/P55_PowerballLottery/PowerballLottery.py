import random

print("Enter 5 different numbers from 1 to 69, with spaces betwee")
print("ach number. (For example: 5 17 23 42 50 51)")
while True:
    response = str(input("> "))
    first_five_number = response.split()
    if len(first_five_number)!=5:
        print("Please enter 5 numbers, separated by spaces.")
        continue
    try:
        valid = True
        for i in range(5):
            first_five_number[i] = int(first_five_number[i])
            if not (1<= int(first_five_number[i]) <=69):
                print("The numbers must all be between 1 and 69.")
                valid = False
        if not valid :
            continue
    except ValueError:
        print("Please enter numbers, like 27, 35, or 62")
        continue
    if len(set(first_five_number)) !=5 : 
        print("You must enter 5 different numbers")
        continue
    break

print("Enter the powerball number from 1 to 26")
while True:
    response = (input("> "))
    try: 
        sixth_number = int(response)
        if not (1<= sixth_number <=69):
            print("The powerball number most be between 1 and 26.")
            continue
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue
    break

print("How many times do you want to play? (Max: 1000000)")
while True:
    response = (input("> "))
    try: 
        roundes = int(response)
        if not (1<= roundes <=1000000):
            print("The number of rounded most be between 1 and 1000000.")
            continue
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue
    break

print(f"It costs ${roundes*2} to play {roundes} times, but don't")
print("worry. I'm sure you'll win it all back")

input("Press Enter to start...")

possiableNumbers = list(range(1,70))
for i in range(roundes):
    random.shuffle(possiableNumbers)
    winningNumber = possiableNumbers[:5]
    winningPowerball = possiableNumbers[-1]
    print(f"The winning Numbers are : {winningNumber} and {winningPowerball}", end="")
    if (set(first_five_number) == set(winningNumber)) and winningPowerball == sixth_number:
        print()
        print('You have won the Powerball Lottery! Congratulations,')
        print('you would be a billionaire if this was real!')
        break
    else:
        print(' You lost.')
print('You have wasted', f"${roundes*2}")
print("Thanks for playing.")