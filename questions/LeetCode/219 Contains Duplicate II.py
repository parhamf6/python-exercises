class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = set()
        l = 0
        for r in range(len(nums)):
            if r - l >k:
                n.remove(nums[l])
                l+=1
            if nums[r] in n:
                return True
            n.add(nums[r])
        return False
