# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/python
def wave(people):
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            waved = people[:i] + people[i].upper()+ people[i+1:]
            result.append(waved)
    return result