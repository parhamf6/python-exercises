class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = len(height)
        ans = []
        for i in range(1,n):
            if height[i-1]>threshold:
                ans.append(i)
        return ans