class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(0.05*len(arr))
        return mean(arr[n : len(arr) - n])
        