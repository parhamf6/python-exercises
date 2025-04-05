import random
from ChoseLevel import *

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 3-10 chances to guess the correct number.")


easyl = [0]
medl = [0]
hardl = [0]
level_list = chose_level()
game_level = int(level_list[0])
game_level_name = level_list[1]
game_level_chance = int(level_list[2])

print(f"Great! You have selected the {game_level_name} difficulty level.")
print("Let's start the game!")

number_of_guesses = 0
currect_or_wrong = 0

user_guit = "y"

while user_guit!="n":
    if number_of_guesses<game_level_chance:
        random_number = random.randrange(1,100)
        user_input = int(input("Enter your guess: "))
        if user_input!=random_number:
            if user_input>random_number:
                print(f"Incorrect! The number is less than {user_input}.")
            else:
                print(f"Incorrect! The number is greater than {user_input}.")
            number_of_guesses+=1
        else:
            print(f"Congratulations! You guessed the correct number in {number_of_guesses} attempts.")
            currect_or_wrong+=1
            ask_to_play = (input("Do You Want tO Play ANother Raound (y/n) :"))
            user_guit = ask_to_play
            number_of_guesses=0
    else:
        print(f"You Out Of Lock The answer Is {random_number}")
        ask_to_play = (input("Do You Want tO Play ANother Raound (y/n) :"))
        user_guit = ask_to_play
        number_of_guesses=0

print("Good Game,Good Luck")









































            # if game_level==1:
            #     easyl.append(number_of_guesses)
            # elif game_level==2:
            #     medl.append(number_of_guesses)
            # else:
            #     hardl.append(number_of_guesses)
            # number_of_guesses=0
            # print(f"Highest Score =>\n Easy : {easyl[0]}\nMedium : {medl[0]}\nHard : {hardl[0]}")









# while currect_or_wrong!=1:
#     if game_level==1:
#         if number_of_guesses<10:
#             user_input = int(input("Enter your guess: "))
#             if user_input!=random_number:
#                 if user_input>random_number:
#                     print(f"Incorrect! The number is less than {user_input}.")
#                 else:
#                     print(f"Incorrect! The number is greater than {user_input}.")
#             else:
#                 print(f"Congratulations! You guessed the correct number in {number_of_guesses} attempts.")
#                 currect_or_wrong=1
#         else:
#             print(f"You Out Of Lock The answer Is {random_number}")
#             break
#     elif game_level==2:
#         if number_of_guesses<5:
#             user_input = int(input("Enter your guess: "))
#             if user_input!=random_number:
#                 if user_input>random_number:
#                     print(f"Incorrect! The number is less than {user_input}.")
#                 else:
#                     print(f"Incorrect! The number is greater than {user_input}.")
#             else:
#                 print(f"Congratulations! You guessed the correct number in {number_of_guesses} attempts.")
#                 currect_or_wrong=1
#         else:
#             print(f"You Out Of Lock The answer Is {random_number}")
#             break
#     elif game_level==3:
#         if number_of_guesses<3:
#             user_input = int(input("Enter your guess: "))
#             if user_input!=random_number:
#                 if user_input>random_number:
#                     print(f"Incorrect! The number is less than {user_input}.")
#                 else:
#                     print(f"Incorrect! The number is greater than {user_input}.")
#             else:
#                 print(f"Congratulations! You guessed the correct number in {number_of_guesses} attempts.")
#                 currect_or_wrong=1
#         else:
#             print(f"You Out Of Lock The answer Is {random_number}")
#             break
#     number_of_guesses+=1






