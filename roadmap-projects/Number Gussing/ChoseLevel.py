level_chance={
    "1":"10",
    "2":"5",
    "3":"3"
}
level_name = {
    "1":"Easy",
    "2":"Medium",
    "3":"Hard"
}
def chose_level():
    print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    choice = input("Enter your choice: ")
    level_list = [choice,level_name[str(choice)],level_chance[str(choice)]]
    return level_list