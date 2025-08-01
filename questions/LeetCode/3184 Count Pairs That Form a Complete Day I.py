from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        i = 0
        j = 1
        c = 0
        while i < len(hours) - 1: 
            if j < len(hours): 
                time = hours[i] + hours[j]
                if time % 24 == 0:
                    c += 1
                if j == len(hours) - 1:  
                    i += 1
                    j = i + 1
                else:
                    j += 1
            else:
                break
        return c
