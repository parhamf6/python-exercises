n = int(input())
power = 0
while n>=(2**power):
    power = power + 1
if n<(2**power):
    print(2**power)