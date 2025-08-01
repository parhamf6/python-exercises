class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        find = 0
        for i in range(len(word)):
            if word[i]==ch:
                find = i
                break
        if find!=-1:
            part1 = word[:find+1]
            part2 = word[find+1:]
            revp1 = part1[::-1]
            ans = revp1 + part2
            return ans
        else:
            return word