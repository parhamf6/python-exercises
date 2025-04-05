
def Enigma():
    keys = "abcdefghijklmnopqrstuvwxyz !"
    values = keys[-1] + keys[0:-1]
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
    msg = input("Please enter your message : ")
    mode = input("Please chose your crypto mode: encode (e) OR decode (d) : ")
    if mode.lower()=="e":
        new_msg = [dict_e[letter] for letter in msg.lower()]
    elif mode.lower()=="d":
        new_msg = [dict_d[letter] for letter in msg.lower()]
    return ("".join(new_msg))

print(Enigma())