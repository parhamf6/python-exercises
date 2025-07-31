class Solution:
    def fib(self, n: int) -> int:
        f = 0
        l = 1
        for i in range(n):
            ln = f + l
            f = l
            l = ln
        return(f)