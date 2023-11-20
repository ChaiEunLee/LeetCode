class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        # 첫행,첫열에 0이 있는지 체크 & 첫행,첫열 중에 0으로 만들어야하는 애들은 다 0으로 만듦.
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
                        
        # 1~부터 돌면서, 첫행,첫열에 0이 있다면 그 행,열을 다 0을 만들어버림.
        for row in range(1,m):
            for col in range(1,n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        print(matrix)
        
        # 왜 따로 첫행,첫열을 보는거지? : 첫행, 첫열을 기준으로 다른 행열을 채워서 첫행, 첫열은 0이 안 되나봄. 
        # 첫행, 첫열이 0이면 첫행, 첫열을 다 0으로 만들어버림.
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0