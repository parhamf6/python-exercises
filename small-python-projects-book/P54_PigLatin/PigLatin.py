
while True:
    response = str(input("Enter your message : "))
    if response=="":
        print("Please type something")
    else:
        break
message = response
vowels = ["a" ,"e" ,"i" ,"o" ,"u" ,"y"]
pigLatin = ""

for word in message.split(" "):
    prefixNonLetter = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetter += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin = pigLatin + prefixNonLetter + " "
    
    suffixNonLetter = ""
    while len(word) > 0 and not word[-1].isalpha():
        suffixNonLetter += word[-1]
        word = word[:-1]
    
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower()
    
    constants = ""
    while len(word) > 0 and word[0] not in vowels:
        constants += word[0]
        word= word[1:]
    
    if constants!="":
        word += constants + 'ay'
    else:
        word += "yay"
    
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    pigLatin += prefixNonLetter+word+suffixNonLetter+" "

print(pigLatin)