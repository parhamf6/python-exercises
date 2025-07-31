class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s+= sum(arr[i:j+1])
        return s 

