class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for num in nums1[:]:
                    nums1.remove(num)
        else:
            for num in nums1[:(m)-1:-1]:
                    nums1.remove(num)

        
        for y in nums2:
            nums1.append(y)
        nums1.sort()