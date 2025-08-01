class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        ans = 1
        if n%2==0:
            ans = 1 * n
        else:
            ans = 2 * n
        return ans