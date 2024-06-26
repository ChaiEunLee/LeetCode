class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False
        
        # 첫 행의 맨뒤
        row = 0
        col = len(matrix[0])-1
        
        while row<=len(matrix)-1 and col>=0:
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                col -= 1
            elif target>matrix[row][col]:
                row += 1
        return False