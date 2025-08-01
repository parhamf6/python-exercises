class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elemsum = 0
        for i in nums:
            elemsum = elemsum + i
        diglist = []
        for z in nums:
            diglist.append(str(z))

        digstr = "".join(diglist)
        digsum=0
        for x in digstr:
            digsum = digsum + int(x)
        return abs(elemsum-digsum)