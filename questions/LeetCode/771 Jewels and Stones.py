class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a = 0
        for i in stones:
            if i in jewels:
                a+=1
        return a