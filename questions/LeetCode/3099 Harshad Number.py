class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        sums = 0
        for i in s:
            sums +=int(i)
        if x%sums==0:
            return sums
        else:
            return -1

