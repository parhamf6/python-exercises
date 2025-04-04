class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ir = 0
        iw = 0
        k = 0
        while (ir < len(nums)):
            if nums[ir]!=val:
                k+=1
                nums[iw]=nums[ir]
                iw +=1
            ir+=1
        return k