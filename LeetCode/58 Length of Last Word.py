class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = s.rsplit(" ")
        zlist = []
        for i in slist :
            if i!="":
                zlist.append(i)
        last = len(zlist[-1])
        return last