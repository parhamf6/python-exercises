class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        list1 = []
        list2 = []
        num1 = 0
        num2 = 0
        for i in range(1,n+1):
            if i%m==0:
                list2.append(i)
            else:
                list1.append(i)
        for n1 in list1:
            num1 = num1 + n1
        for n2 in list2:
            num2 = num2 + n2
        ans = num1 - num2
        return ans