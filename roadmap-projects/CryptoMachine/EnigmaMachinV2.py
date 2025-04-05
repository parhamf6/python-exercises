import random
import json

with open(r"LearningProjects\Python\RoadMapProjects\CryptoMachine\UserData.json" , "r") as f:
    user_data = dict(json.load(f))
keys = "abcdefghijklmnopqrstuvwxyz"
use_value = user_data["admin"]
def key_build():
    global keys , values
    keys = "abcdefghijklmnopqrstuvwxyz"
    random_choice = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    values = ""
    for i in range(len(keys)):
        x = random.choice(random_choice)
        random_choice.remove(x)
        values = values + str(x)
    return keys , values

def add_user():
    x = 0
    while x !=1:
        user_name = input("Please Enter your user name : ")
        if user_name not in user_data:
            key_build()
            user_data[f"{user_name}"] = f"{values}"
            with open(r"LearningProjects\Python\RoadMapProjects\CryptoMachine\UserData.json" , "w") as f:
                json.dump(user_data,f)
            x = 1
        else:
            print("User name is already exist please chose another user name")

def see_key():
    user_see = input("Please enter your user name : ")
    i = user_data[user_see]
    print(f"Your Key is {i}")

def remove():
    user_out = input("please enter your user name :")
    user_data.pop(f'{user_out}')
    print(f"The {user_out} user name in deleted from data base")

def Enigma():
    z = 0
    while z!=1:
        input_user = input("Please Your user name : ")
        if input_user in user_data:
            use_value = user_data[f"{input_user}"]
            dict_e = dict(zip(keys,use_value))
            dict_d = dict(zip(use_value,keys))
            msg = input(r"Please enter your message : ")
            mode = input("Please chose your crypto mode: encode (e) OR decode (d) : ")
            if mode.lower()=="e":
                new_msg = [dict_e.get(letter, '?') for letter in msg.lower()]
            elif mode.lower()=="d":
                new_msg = [dict_d.get(letter, '?') for letter in msg.lower()]
            return ("".join(new_msg))
            z = 1
            break
        else:
            print("Your User name is not in the user data please chose another user name")
            # e = input("Do you Want to chose another or go back to build ? : \n back : 5 \n another name : 6 ")


m = 0
while m!=1:
    print("Enigma : 1 \n Add user : 2 \n Remove User : 3 \n Close : 4")
    user_input = int(input("Please Select What you Want to Do ? : "))
    if user_input==1:
        print(Enigma())
    elif user_input==2:
        add_user()
    elif user_input==3:
        remove()
    elif user_input==4:
        m=1
        print("Good Luck")






