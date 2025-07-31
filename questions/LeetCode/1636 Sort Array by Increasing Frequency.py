from collections import Counter
from heapq import heappop, heappush
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        heap = []
        for num in freq:
            heappush(heap, (freq[num], -num))

        output = []
        while heap:
            f, n = heappop(heap)
            for i in range(f):
                output.append(-n)
        
        return output
        