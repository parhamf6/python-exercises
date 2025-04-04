class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.rsplit(" ")
        revl = []
        for i in slist:
            x = i[::-1]
            revl.append(x)
        return (" ".join(revl))