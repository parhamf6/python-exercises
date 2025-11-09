class Solution(object):
    def countOperations(self, num1, num2):
        c = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            c += 1
        return c