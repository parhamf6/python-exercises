user = str(input())
for i in user :
    if user[0:1]=="Y":
        print("Haji")
        break
    if user[1:2] == "Y":
        print("Karbalaee")
        break
    if user[2:3]=="Y":
        print("Mashti")
        break
    else :
        print("Agha")
        break