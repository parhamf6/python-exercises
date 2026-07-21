# More advance version
import random

all_letters = "abcdefghijklmnopqrstuvwxyz"

def main():
    key = None
    while True:
        print("Choose your mode:")
        print("e for Encrypt")
        print("d for Decrypt")
        print("n for new key")
        print("q for Quit")
    
        response = input("> ").lower()
        if response == "q":
            print("\nGoodby")
            break
        elif response == "n":
            key = get_key()
        
        elif response == "e":
            if key is None:
                print("You mos first set a key")
                key = get_key()
            new_msg = encrypt_msg(key)
            print(new_msg)
        elif response == "d":
            if key is None:
                print("You mos first set a key")
                key = get_key()
            new_msg = decrypt_msg(key)
            print(new_msg)
        else:
            print("invalid option")

def get_key():
    while True:
        print("please provide the key or use RANDOM to generate new key")
        response = input("> ")
        if response.lower() == "random":
            key = generate_new_key()
            print("New key generated successfully")
            print(key.upper())
            break
        else:
            valid_status = check_valid_key(response)
            if valid_status:
                key = str(response.lower())
                print("Key Validate Successfully")
                break
            elif not valid_status:
                print("Please provide a valid key or generate new one.")
                continue
    return key

def generate_new_key():
    all_letters_indexes = list(range(0,26))
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    random.shuffle(all_letters_indexes)
    new_key = ""
    for i in all_letters_indexes:
        new_key+=all_letters[i]
    return new_key
    
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
            encrypted_msg+=new_letter.upper()
        elif i.islower():
            letter_index = all_letters.index(i)
            new_letter = key[letter_index]
            encrypted_msg+=new_letter
        else:
            encrypted_msg+=i
    return encrypted_msg
        
def decrypt_msg(key):
    print("Please enter your message to decrypt.")
    encrypted_msg = input("> ")
    decrypted_msg = ""
    for i in encrypted_msg:
        if i.isupper():
            letter_index = key.index(i.lower())
            new_letter = all_letters[letter_index]
            decrypted_msg+=new_letter.upper()
        elif i.islower():
            letter_index = key.index(i)
            new_letter = all_letters[letter_index]
            decrypted_msg+=new_letter
        else:
            decrypted_msg+=i
    return decrypted_msg
        
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoogbye")