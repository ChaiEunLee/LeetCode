class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = len(matrix)
        col_num = len(matrix[0])
        
        begin, end = 0, row_num*col_num-1
        while begin<=end:
            mid = begin+(end-begin)//2
            mid_value = matrix[mid//col_num][mid%col_num]
            
            if mid_value==target:
                return True
            elif mid_value<target:
                begin = mid+1
            else:
                end = mid-1
        return False