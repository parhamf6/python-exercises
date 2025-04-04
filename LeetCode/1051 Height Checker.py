class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        unsort = heights.copy()
        heights.sort()
        c = 0
        for i in range(len(heights)):
            if unsort[i]!=heights[i]:
                c+=1
        return c