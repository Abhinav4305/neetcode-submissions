class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==target:
                    return True
        return False

        ROW = len(matrix)
        COl = len(matrix[0])

        r, c = 0, (ROW*COL - 1)
        while r <= c:
            m = l + ((r - l)//2)
            if target > matrix[r][c]:
                l = m + 1
            elif target < matrix[r][c]:
                r = m - 1
            else:
                return True
        return False
        