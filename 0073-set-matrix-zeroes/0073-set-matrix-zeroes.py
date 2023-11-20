class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        
        # 0이 있는 row, col을 기록
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True
                    
        # 0이 있는 row, col을 다 0으로 만듦
        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0