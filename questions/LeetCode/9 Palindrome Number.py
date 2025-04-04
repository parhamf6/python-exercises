class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for r1 in range(len(nums)):
            for r2 in range(r1 + 1, len(nums)):
                if nums[r1] + nums[r2] == target:
                    return [r1, r2]
        return []
