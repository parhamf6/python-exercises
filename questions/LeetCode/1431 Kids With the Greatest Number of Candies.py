class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        ans = []
        for i in candies :
            x = i + extraCandies
            if x >= maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans