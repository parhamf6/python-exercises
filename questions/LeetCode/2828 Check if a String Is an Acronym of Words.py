class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        r = ""
        for i in words:
            r=r+i[0]
        if r==s:
            return True
        else:
            return False