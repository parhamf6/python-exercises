# https://www.codewars.com/kata/5262119038c0985a5b00029f/python
def is_prime(num):
    if num>2:
        for i in range (2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    elif num==2:
        return True
    else:
        return False