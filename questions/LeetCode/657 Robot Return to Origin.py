class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for i in moves:
            if i=="U":
                x = x +1
            elif i=="D":
                x = x - 1
            elif i=="R":
                y = y + 1
            elif i=="L":
                y = y - 1
        if x==0 and y==0:
            return(True)
        else:
            return(False)
