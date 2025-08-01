class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        lsp = [nums[0]]

        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1] + 1:
                lsp += [nums[i]]
                i += 1
            else:
                break
        s = 0
        for i in range(0,len(lsp)):
            s += lsp[i]
        
        si = s
        while nums.count(si) != 0:
            si = si + 1

        return si