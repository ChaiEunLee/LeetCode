class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols-1
        
        while (row<rows and col>-1):
            cur = matrix[row][col]
            if cur==target:
                return True
            if target>cur:
                row +=1
            else:
                col -=1
                
        return False