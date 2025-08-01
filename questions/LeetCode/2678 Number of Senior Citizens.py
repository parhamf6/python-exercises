class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            a = i[-4:-2]
            if int(a)>60:
                c+=1
        return c
