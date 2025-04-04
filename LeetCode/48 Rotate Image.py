class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        edgeLength = len(matrix)
        top = 0
        bottom = edgeLength - 1
        while top < bottom:
            for col in range(edgeLength):
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
            top += 1
            bottom -= 1
        for row in range(edgeLength):
            for col in range(row + 1, edgeLength):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]