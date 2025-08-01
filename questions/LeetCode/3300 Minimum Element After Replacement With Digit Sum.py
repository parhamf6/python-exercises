class Solution:
    def minElement(self, nums: List[int]) -> int:
        nlist = []
        for i in nums:
            x = str(i)
            s = 0
            for j in x:
                s = s + int(j)
            nlist.append(s)

        return (min(nlist))
