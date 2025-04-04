class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums.reverse()
        nlist = []
        for i in nums:
            if i not in nlist:
                nlist.append(i)

        if len(nlist)>=3:
            return(nlist[2])
        elif len(nlist)<3:
            return(nlist[0])
