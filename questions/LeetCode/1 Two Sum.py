# version 1: brute force
# Check every possible pair.
# Simple but slow because the number of comparisons grows quadratically.
# Time: O(n^2), Space: O(1)
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


# version 2: improved but still slow
# Instead of checking every pair, we search for the complement.
# However, list lookup is O(n), and slicing also costs O(n).
# We repeat these searches inside a loop.
# Time: O(n^2), Space: O(n) because of slicing.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                out.append(i)
                second_index = nums[i+1:].index(target-nums[i])+ len(nums[:i+1])
                out.append(second_index)
                break
        return out

# version 3: optimal
# Store previously seen numbers in a dictionary.
# Dictionary lookup is O(1) average, so we only scan the list once.
# Time: O(n), Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = {}
        for i in range(len(nums)):
            need = target-nums[i]
            if need in out:
                return[out[need], i]
            out[nums[i]]=i
