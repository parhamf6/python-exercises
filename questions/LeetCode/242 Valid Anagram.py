class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = 0
        for i in s:
            if s.count(i)==t.count(i):
                c += 1
        if c==len(s) and len(s)==len(t):
            return True
        else:
            return False