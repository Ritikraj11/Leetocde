class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute Force 

        # n = len (matrix)
        # mat = [[0 for _ in range(4)] for _ in range(4)]
        # for i in range (0,n):
        #     for j in range(0,n):
        #         mat[j][(n-1)-i] = matrix[i][j]

        n = len(matrix)
        for i in range (0,n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(0,n):
            matrix[i] = matrix[i][::-1]
