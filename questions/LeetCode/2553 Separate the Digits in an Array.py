class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            for j in str(i):
                ans.append(int(j))
        return ans