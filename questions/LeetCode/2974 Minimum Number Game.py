class Solution:
    def numberGame(self, nums):
        n = len(nums)

        nums.sort()

        i = 0

        while i < n-1:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2 

        return nums
        