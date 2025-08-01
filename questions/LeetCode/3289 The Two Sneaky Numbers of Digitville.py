class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums.count(i)>1 and i not in ans:
                ans.append(i)
        return ans

