class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        bigNum = max(nums)

        for num in nums:
            if num == bigNum:
                continue  
            elif bigNum - (num*2) < 0:
                return -1  
        
        return nums.index(bigNum)  
                