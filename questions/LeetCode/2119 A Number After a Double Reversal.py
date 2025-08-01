class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        original=num
        reverse1=0
        while num!=0:
            reverse1=(num%10)+reverse1*10
            num//=10
        reverse2=0
        while reverse1!=0:
            reverse2=(reverse1%10)+reverse2*10
            reverse1//=10
        if(reverse2==original):
            return True
        else:
            return False
        