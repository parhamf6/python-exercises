class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for i in words:
            x = i.rsplit(separator)
            for w in x:
                if w!="":
                    ans.append(w)
        return ans
