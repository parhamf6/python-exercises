class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(word1)+len(word2)
        c = 0
        ans = ""
        while c<=l:
            if c<len(word1):
                ans = ans + word1[c]
            if c<len(word2):
                ans = ans + word2[c]
            c = c + 1
        return ans
