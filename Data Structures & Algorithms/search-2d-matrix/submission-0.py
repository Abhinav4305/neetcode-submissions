class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])-1):
                if matrix[i][j]==target:
                    return True
            return False