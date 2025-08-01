class Solution:
    def minimumChairs(self, s: str) -> int:
        tem = []
        c = 0
        for i in s:
            if i=="E":
                c+=1
            else:
                c-=1
            tem.append(c)
        return (max(tem))