def main():
    print("chose The mode to decrypt or encrypt the message")
    print("please chose the mode")
    print("a or A for encrypt")
    print("b or B for decrypt")
    while True:
        response = input("Chose the mode > ")
        valid_inputes = ["a", "A", "b", "B"]
        if response in valid_inputes:
            mode = str(response).lower()
            break
        else:
            print("Please provide input with one of this  a,A,b,B.")
            continue
    if mode=="a":
        encrypt_cipher()
    elif mode=="b":
        decrypt_cipher()


def find_rot13(letter):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_index = lower_letters.find(letter)
    rot_index = (letter_index+13) % 26
    rot_letter = lower_letters[rot_index]
    return rot_letter
    

def encrypt_cipher():
    msg = input("Please enter you message to encrypt > ")
    encrypter_msg = []
    for i in msg:
        if i.isalpha():
            letter = find_rot13(i.lower())
            if i.isupper():
                encrypter_msg.append(letter.upper())
            else:
                encrypter_msg.append(letter)
        else:
            encrypter_msg.append(i)
    print("".join(encrypter_msg))
    print("-------")
        
            
def decrypt_cipher():
    msg = input("Please enter you message to decrypt > ")
    encrypter_msg = []
    for i in msg:
        if i.isalpha():
            letter = find_rot13(i.lower())
            if i.isupper():
                encrypter_msg.append(letter.upper())
            else:
                encrypter_msg.append(letter)
        else:
            encrypter_msg.append(i)
    print("".join(encrypter_msg))
    print("-------")
    
    
while True:
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodBye")
        break