# ماشین متنی قدیمی
# https://quera.org/problemset/307
s = str(input())
exit = False

while not exit:
    command_list = str(input()).split(" ")
    if command_list[0]=="SHIFT-R":
        n = int(command_list[-1])*-1
        last_part = s[n:]
        s = last_part+s[:n]
    elif command_list[0]=="SHIFT-L":
        n = int(command_list[-1])
        last_part = s[:n]
        s = s[n:]+last_part
    elif command_list[0]=="EXTEND":
        n = int(command_list[-1])
        s = s + f"{"*"*n}"
    elif command_list[0]=="SHRINK":
        n = int(command_list[-1])
        if len(s)<n:
            s=""
        else:
            s = s[:-n]
    elif command_list[0]=="REVERSE":
        s = s[::-1]
    elif command_list[0]=="PUT":
        pos = int(command_list[-2])
        char = command_list[-1]
        s = s[:pos-1]+char+s[pos:]
    elif command_list[0]=="PRINT":
        print(s)
    elif command_list[0]=="EXIT":
        exit = True