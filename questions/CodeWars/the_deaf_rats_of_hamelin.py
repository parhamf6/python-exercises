# https://www.codewars.com/kata/598106cb34e205e074000031/python
import re
def count_deaf_rats(town):
    town = town.replace(" ", "")
    loc = town.index("P")
    if town[0] == "P":
        right = town[1:]
        rats = [right[i:i+2] for i in range(0, len(right), 2)]
        return sum(r == "~O" for r in rats)
    elif town[-1] == "P":
        left = town[:-1]
        rats = [left[i:i+2] for i in range(0, len(left), 2)]
        return sum(r == "O~" for r in rats)
    else:
        bef = town[:loc]
        aft = town[loc+1:]
        bef_rats = [bef[i:i+2] for i in range(0, len(bef), 2)]
        aft_rats = [aft[i:i+2] for i in range(0, len(aft), 2)]
        matbef = sum(r == "O~" for r in bef_rats)
        mataft = sum(r == "~O" for r in aft_rats)
        return matbef + mataft