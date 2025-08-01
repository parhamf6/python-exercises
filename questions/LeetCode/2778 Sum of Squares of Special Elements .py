class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sqsum = 0
        n = len(nums)
        for i in range(1,n+1):
            if n%(i)==0:
                x = nums[i-1]
                sqsum+=(x**2)
        return sqsum