class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Initialize the count of unique elements to 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Overwrite the next unique element
                k += 1
        
        return k