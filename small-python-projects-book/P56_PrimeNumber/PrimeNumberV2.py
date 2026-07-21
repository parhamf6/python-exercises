# More advanced version
# 
from math import sqrt
from sys import exit

print("Please chose your mode a or A for A, and b or B for B.")
print("A: See every prime number in a range,")
print("B: see every prime number from start to the time you chose to stop,")

def main():
    while True:
        response = input("> ")
        valid_inputes = ["a", "A", "b", "B"]
        if response in valid_inputes:
            mode = str(response).lower()
            break
        else:
            print("Please provide input with one of this  a,A,b,B.")
            continue
    if mode=="a":
        rangeMode()
    elif mode=="b":
        infiniteMode()

def rangeMode():
    print('Enter two number as start and end of range seperated by space like 1 5')
    print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
    while True:
        response = input("> ")
        start, end = response.split()
        if start.isdecimal() and end.isdecimal():
            start_n = int(start)
            end_n = int(end)
            break
        else:
            print("Please provide a number like 2, 2222, etc.")
    
    input('Press Ctrl-C at any time to quit. Press Enter to begin...')
    
    while True:
        for i in range(start_n, end_n):
            if isPrime(i):
                print(str(i) + ', ', end="", flush=True)
        break
            

def infiniteMode():
    print('Enter a number to start searching for primes from:')
    print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
    while True:
        response = input("> ")
        if response.isdecimal():
            num = int(response)
            break
        else:
            print("Please provide a number like 2, 1999, etc.")
            continue
    
    input('Press Ctrl-C at any time to quit. Press Enter to begin...')
    
    while True:
        if isPrime(num):
            print(str(num) + ', ', end="", flush=True)
        num = num+1

def isPrime(number):
    if number < 2:
        return False
    
    elif number==2:
        return True
    
    for i in range(2,int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()