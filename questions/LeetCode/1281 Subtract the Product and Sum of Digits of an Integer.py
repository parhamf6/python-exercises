class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumd = 0
        prod = 1
        c = str(n)
        for i in c:
            x =  int(i)
            sumd = sumd + x
            prod = prod * x
        return (prod-sumd)