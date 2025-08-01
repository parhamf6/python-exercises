class Solution:
    def minimumSum(self, num: int) -> int:
        nlist = []
        for i in str(num):
            nlist.append(i)
        nlist.sort()
        new1 = nlist[0]+nlist[2]
        new2 = nlist[1]+nlist[3]
        return(int(new1)+int(new2))