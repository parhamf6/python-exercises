class Solution:
    def countDigits(self, num: int) -> int:
        strn = str(num)
        c = 0
        for i in strn:
            if num%(int(i))==0:
                c = c + 1
        return c