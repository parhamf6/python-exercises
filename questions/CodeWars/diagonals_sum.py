# https://www.codewars.com/kata/5592fc599a7f40adac0000a8/python
def sum_diagonals(matrix):
    rl = 0
    lr = 0
    for i in range(len(matrix)):
        if i==0:
            rl+=matrix[i][i]
            lr+=matrix[i][-1]
        else:
            rl+=matrix[i][i]
            lr+=matrix[i][-i-1]
    return rl+lr