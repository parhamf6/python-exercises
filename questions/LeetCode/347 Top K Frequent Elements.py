class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i]=nums.count(i)
        asc = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        return list(asc.keys())[:k]
