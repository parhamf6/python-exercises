import random

letters = {
    'a' : ['4','@',r'/-\\'],
    'c' : ['('],
    'd' : ['|)'],
    'e' : ['3'],
    'f' : ['ph'],
    'h' : [']-[','|-|'],
    'i' : ['1', '!', '|'],
    'k' : [']<'],
    'o' : ['0'],
    's' : ['$', '5'],
    't' : ['7', '+'],
    'u' : ["|_|"],
    'v' : [r'\\/'],
}

msg = str(input("PLease input your message : "))
ans = []
for i in msg:
    i.lower()
    if i in letters:
        x = letters[i]
        z = random.choice(x)
        ans.append(z)
    else:
        ans.append(i)
print("".join(ans))