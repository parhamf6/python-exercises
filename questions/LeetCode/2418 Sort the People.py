class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        sorted_index = sorted(list(range(n)), key= lambda x:heights[x],reverse=True)
        ans = []
        for i in sorted_index:
            ans.append(names[i])
        return ans


