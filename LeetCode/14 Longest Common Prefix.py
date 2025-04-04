class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        min_length = float('inf')
        for s in v:
            if len(s) < min_length:
                min_length = len(s)
        i = 0
        while i < min_length :
            for s in v:
                if s[i]!=v[0][i]:
                    return s[:i]
            i+=1
        return s[:i]
