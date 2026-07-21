class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        dup = False
        for i in nums:
            if i in seen:
                dup = True
                return dup
            else:
                seen[i] = i
        return dup
            
