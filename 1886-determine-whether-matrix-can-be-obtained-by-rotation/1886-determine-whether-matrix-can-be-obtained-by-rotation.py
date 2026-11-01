class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:

        n = len(mat)
        def rotate(matrix):
            for i in range(0,n-1):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            for i in range(0,n):
                matrix[i].reverse()
            return matrix
        
        for i in range(0,4):
            if mat == target:
                return True
            rotate(mat)

        return (False)