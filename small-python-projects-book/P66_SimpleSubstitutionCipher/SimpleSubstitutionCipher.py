import random
def main():
    # Chose the mode
    while True:
        print("Chose your mode (e)ncrypt (d)ecrypt")
        response = input("> ")
        if response.lower() in ["e", "d"]:
            mode = str(response).lower()
            break
        else:
            print("please enter e or d")
            continue
    
    # the key status
    while True:
        print("please provide the key or use RANDOM to generate new key")
        response = input("> ")
        if response.lower() == "random":
            key = generate_new_key()
            print("New key generated successfully")
            print(key)
            break
        else:
            valid_status = check_valid_key(response)
            if valid_status:
                key = str(response)
                print("Key Validate Successfully")
                break
            elif not valid_status:
                print("Please provide a valid key or generate new one.")
                continue
                
    
    if mode=="e":
        new_msg = encrypt_msg(key)
        print(new_msg)
    elif mode=="d":
        new_msg = decrypt_msg(key)
        print(new_msg)
        

all_letters = "abcdefghijklmnopqrstuvwxyz"
    
def generate_new_key():
    all_letters_indexes = list(range(0,26))
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    random.shuffle(all_letters_indexes)
    new_key = ""
    for i in all_letters_indexes:
        new_key+=all_letters[i]
    return new_key.upper()
def check_valid_key(key_candidate):
    if len(key_candidate)==26 and key_candidate.isalpha():
        return True
    else:
        return False
        
def encrypt_msg(key):
    print("Please enter your message to encrypt.")
    msg = input("> ")
    encrypted_msg = ""
    for i in msg:
        if i.isupper():
            letter_index = all_letters.index(i.lower())
            new_letter = key[letter_index]
            encrypted_msg+=new_letter
        elif i.islower():
            letter_index = all_letters.index(i.lower())
            new_letter = key[letter_index]
            encrypted_msg+=new_letter.lower()
        else:
            encrypted_msg+=i
    return encrypted_msg
        
def decrypt_msg(key):
    print("Please enter your message to decrypt.")
    encrypted_msg = input("> ")
    decrypted_msg = ""
    for i in encrypted_msg:
        if i.isupper():
            letter_index = key.index(i.upper())
            new_letter = all_letters[letter_index]
            decrypted_msg+=new_letter.upper()
        elif i.islower():
            letter_index = key.index(i.upper())
            new_letter = all_letters[letter_index]
            decrypted_msg+=new_letter
        else:
            decrypted_msg+=i
    return decrypted_msg
        
if __name__=="__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\nGoogbye")
            break