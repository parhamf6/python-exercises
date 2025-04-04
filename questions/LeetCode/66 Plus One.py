class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        st = ""
        ans = []
        for i in digits:
            st = st + str(i)
        x = int(st)+1
        for c in str(x):
            ans.append(int(c))
        return ans