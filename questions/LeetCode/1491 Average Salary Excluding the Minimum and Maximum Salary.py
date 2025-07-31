class Solution:
    def average(self, salary: List[int]) -> float:
        s = sum(salary)
        salary.sort()
        s = s -salary[0]-salary[-1]
        return(s/(len(salary)-2))