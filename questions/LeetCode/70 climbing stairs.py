class Solution:
    def climbStairs(self, n: int) -> int:
        f = 1
        l = 1
        for i in range(0,n):
            ln = f + l
            f = l
            l = ln
        return f
                
                