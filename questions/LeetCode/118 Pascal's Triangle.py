class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        if numRows==1:
            return([[1]])
        elif numRows==2:
            return([[1],[1,1]])
        else:
            for i in range(1,numRows-1):
                tr = res[-1]
                c = []
                for t in range(len(tr)):
                    if t==0:
                        c.append(1)
                    elif t==len(tr)-1:
                        c.append(tr[-1]+tr[-2])
                        c.append(1)
                    else:
                        c.append(tr[t]+tr[t-1])
                res.append(c)
        return(res)
