class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r = 0
        for i in sentences:
            s = (len(i.rsplit(" ")))
            if (s)>r:
                r=s
        return r
