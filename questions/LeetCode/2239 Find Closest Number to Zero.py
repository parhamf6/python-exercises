class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        smallest = 0
        for i in nums:
            if abs(i) == 0:
                return 0
            elif smallest == 0 or abs(i) < abs(smallest):
                smallest = i
            elif abs(i) == abs(smallest):
                if i > smallest:
                    smallest = i
        return smallest