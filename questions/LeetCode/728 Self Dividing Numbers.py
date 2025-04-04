class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        num = 0
        ans = []
        for i in range(left,right+1):
            num = i
            xf = str(num)
            if "0" not in xf:
                c = 0
                for i in xf:
                    if num%(int(i))==0:
                        c+=1
                if c== len(xf):
                    ans.append(num)
        return ans
