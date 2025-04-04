class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for c in columnTitle:
            res = res*26 + ord(c)-ord('A')+1
        return res