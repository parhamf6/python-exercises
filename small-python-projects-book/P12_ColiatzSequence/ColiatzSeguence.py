
sta = 1
while sta!=0:
    number = int(input("\nPlease input the starting number greater then zero or quit(0) : "))
    print(number)
    if number!=0:
        while number!=1:
            if number%2==0:
                number = number/2
            else:
                number = (number*3)+1
            print(', ' + str(int(number)), end='')
            if number==1:
                break
    elif number==0:
        sta=0
        print("Good luck")