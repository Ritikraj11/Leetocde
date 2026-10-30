class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        rowTrack = [0] * r
        colTrack = [0] * c

        for i in range(0,r):
            for j in range (0,c):
                if matrix[i][j] == 0:
                    rowTrack[i] = -1
                    colTrack[j] = -1 
        for i in range(0,r):
            for j in range(0,c):
                if rowTrack[i] == -1 or colTrack[j] == -1:
                    matrix[i][j] = 0
