class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        a = 0
        for i in s:
            a = a + (int(i))
        while a>9:
            sa = str(a)
            a = 0
            for ia in sa:
                a = a +(int(ia))
        return a