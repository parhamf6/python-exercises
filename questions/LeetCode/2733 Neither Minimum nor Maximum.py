class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)>2:
            nums.sort()
            return (nums[1])
        else:
            return -1