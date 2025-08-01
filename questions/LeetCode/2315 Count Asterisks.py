class Solution:
    def countAsterisks(self, s: str) -> int:
        cbars = 0
        cs = 0
        for i in s:
            if i=="|":
                cbars+=1
            if i=="*":
                if cbars%2==0:
                    cs+=1
        return cs