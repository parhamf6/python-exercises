# https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    p=0
    for i in bus_stops:
        p=p+(i[0])
        p=p-(i[1])
    return (p)