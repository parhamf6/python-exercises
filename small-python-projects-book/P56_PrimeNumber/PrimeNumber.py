from math import sqrt
from sys import exit

print('Enter a number to start searching for primes from:')
print('(Try 0 or 1000000000000 (12 zeros) or another number.)')

def main():
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