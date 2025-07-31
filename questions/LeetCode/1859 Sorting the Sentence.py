class Solution:
    def sortSentence(self, s: str) -> str:
        slist = s.rsplit(" ")
        l = len(slist)
        c = 1
        ans = []
        while c<=l:
            for i in slist:
                if f"{c}" in i:
                    i = i.replace(f"{c}", "")
                    ans.append(i)
            c = c + 1
        x = " ".join(ans)
        return(x)