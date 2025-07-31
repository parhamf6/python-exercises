class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sl = s.rsplit(" ")
        tem = []
        for i in range(0,k):
            tem.append(sl[i])
        x = " ".join(tem)
        return x